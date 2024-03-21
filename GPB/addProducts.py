import json

import sys

sys.path.append("./../")
from utils import generate_local_embeddings, generateRandomStringId
from langchain_google_genai import GoogleGenerativeAI

from pinecone import Pinecone, ServerlessSpec
from prompts import (
    genericProductSimilarityPrompt,
    additionalFeaturesPrompt,
    addAdditionalFeaturesPrompt,
    extractGenericProductPrompt,
)

from pymongo.mongo_client import MongoClient

# Replace the placeholder with your Atlas connection string
uri = "mongodb+srv://rj1804567:Ys1frRGMKLjUvtwo@cluster0.rhrpbo1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
pc = Pinecone()
index = pc.Index("tgs-cgp-index")
llm = GoogleGenerativeAI(model="gemini-pro")  # type: ignore
max_retries = 3


def checkProductExist(product):
    # check if the product already exist in db
    # semantic search in index
    product = str(product)
    productEmbeddings = generate_local_embeddings(product)

    if index is None:
        RuntimeError("Index not found")
        return None

    genericProductCandidates = index.query(
        namespace="from-GIST-small",
        vector=productEmbeddings,
        top_k=3,
        # include_values=True,
        include_metadata=True,
    )["matches"]

    # ask LLM if this product is similar to generic product

    for candidate in genericProductCandidates:
        for retry in range(max_retries):
            try:
                result = llm.invoke(
                    genericProductSimilarityPrompt.format(
                        product=product, genericProduct=candidate
                    )
                )
                if result not in ["False", "True"]:
                    print("Invalid response from LLM")
                    raise Exception("Invalid response from LLM")
                if result == "True":
                    return candidate
            except Exception:
                print(f"retry {retry} failed")
                if retry < max_retries - 1:
                    print("Error {e} occurred. Retrying...")
                else:
                    print("Max retries exceeded. Error handling logic here.")
                    raise Exception("Max retries exceeded. Error handling logic here.")
    return None


def addAdditionalFeatures(genericProduct, product) -> object:
    # extract additional features and add to listing

    additionalFeatures = None
    productStr = str(product)
    genericProductStr = str(genericProduct)
    for retry in range(max_retries):
        try:
            result = llm.invoke(
                additionalFeaturesPrompt.format(
                    product=productStr, genericProduct=genericProductStr
                )
            )
            additionalFeatures = json.loads(result)
            additionalFeatures = additionalFeatures["additionalFeatures"]
            break
        except Exception as e:
            if retry < max_retries - 1:
                print(f"An error occurred: {e}")
            else:
                print("Max retries exceeded. Error handling logic here.")
                raise Exception("Max retries exceeded. Error handling logic here.")

    for retry in range(max_retries):
        try:
            # print("additionalFeatures \n " + str(additionalFeatures))
            if "additionalFeatures" in genericProduct:
                result = llm.invoke(
                    addAdditionalFeaturesPrompt.format(
                        currentAdditionalFeatures=str(
                            genericProduct["additionalFeatures"]
                        ),
                        additionalFeatures=str(additionalFeatures),
                    )
                )
                print("result \n " + str(result))
                additionalFeatures = json.loads(result)
                genericProduct["additionalFeatures"].update(additionalFeatures)
            else:
                genericProduct["additionalFeatures"] = additionalFeatures
            return genericProduct
        except Exception:
            if retry < max_retries - 1:
                print("Error occurred. Retrying...")
            else:
                print("Max retries exceeded. Error handling logic here.")
                raise Exception("Max retries exceeded. Error handling logic here.")


def addAdditionalSituations(genericProduct, product) -> object:
    return genericProduct


def generateGenericProduct(product) -> object:
    # generate generic product and features and add to listing
    for retry in range(max_retries):
        try:
            result = llm.invoke(extractGenericProductPrompt.format(product=product))
            genericProduct = json.loads(result)
            # {
            #   "Generic Product Description": "Provide a generic description of the product without brand-specific features or unique selling points.",
            #   "Unique Features List": ["feature1", "feature2", "feature3"]
            # }
            if (
                "Description" not in genericProduct
                or "UniqueFeatures" not in genericProduct
            ):
                raise Exception("Invalid response from LLM")

            return genericProduct
        except Exception:
            if retry < max_retries - 1:
                print("Error {e} occurred. Retrying...")
            else:
                print("Max retries exceeded. Error handling logic here.")
                raise Exception("Max retries exceeded. Error handling logic here.")


def saveProduct(genericProduct, product) -> bool:
    # save all product details to another db

    genericProductVector = generate_local_embeddings(str(genericProduct))
    pineCodeVectors = []
    # !TODO make sure the metadata size is less then 4096 bytes
    # texts = list(filter(lambda x: len(x) <= 40960, texts))
    # https://github.com/langchain-ai/langchain/issues/3800
    genericProductId = generateRandomStringId()
    product["genericProductId"] = genericProductId
    pineCodeVectors.append((genericProductId, genericProductVector, genericProduct))
    if index is not None:
        index.upsert(
            pineCodeVectors,
            namespace="genericProducts",
            id=generateRandomStringId(),
        )
    else:
        return False
    db = client["cluster0"]
    collection = db["products"]
    collection.insert_one(product)
    # collection.insert_one(
    #     {
    #         "data": {
    #             "product": "Pendant Ceramic Lamp",
    #             "description": "Handmade hanging ceiling lamp featuring a unique design with printed decoration of green leaves. Crafted from clay, this light fixture is a piece of art, suitable for living room centers and offices. The lamp comes in various colors and has a height of 17.7 inches and a diameter of 7.9 inches.",
    #             "targetAudience": [
    #                 {
    #                     "targetAudience": "Interior designers and home decorators",
    #                     "useCase": "Adding a unique and stylish lighting fixture to a living room, office, or other space.",
    #                 },
    #                 {
    #                     "targetAudience": "Art collectors",
    #                     "useCase": "Displaying the lamp as a piece of art in a home or gallery.",
    #                 },
    #                 {
    #                     "targetAudience": "People who appreciate handmade and unique items",
    #                     "useCase": "Adding a touch of personality and style to their home with a one-of-a-kind lighting fixture.",
    #                 },
    #             ],
    #         },
    #         "metadata": {
    #             "url": "https://www.etsy.com/listing/724851215/pendant-ceramic-lamp-hanging-ceiling?click_key=bbd6dcdb3b7f27cd427fa99cb073862a0ea919a0%3A724851215&click_sum=2ab64d42&ref=stl_listing-1",
    #             "dateCreated": "2024-02-18T22:31:55.943816",
    #             "productId": "EfJOyTJcIJ",
    #         },
    #     }
    # )
    return True


# Specify the path to your JSON file
def addFile(numbers) -> None:
    file_path = (
        "./../scrappedProductDescription/EstyPersonalisedGiftDescription"
        + str(numbers)
        + ".json"
    )

    # Open the file and load the JSON data
    with open(file_path, "r") as file:
        json_data = json.load(file)

        # Now you can work with the loaded JSON data as a list
        for i, product in enumerate(json_data):
            print("Adding {i}th item to Pinecone" + "\n")
            productTemp = product
            del productTemp["productId"], productTemp["url"]

            # check if the generic product already exist in db
            genericProduct = checkProductExist(productTemp)

            # if yes => extract additional features and add to listing
            if genericProduct is not None:
                genericProductDesc = genericProduct["metadata"]
                del (
                    genericProductDesc["url"],
                    genericProductDesc["productId"],
                    genericProductDesc["dateCreated"],
                )
                genericProduct = addAdditionalFeatures(genericProductDesc, productTemp)
            # if no => generate generic product and features and add to listing
            else:
                genericProduct = generateGenericProduct(productTemp)
            # save all product details to another db

            print("genericProduct " + str(genericProduct) + "\n")
            print("product " + str(product))
            saveProduct(genericProduct, product)
            print("Added {i}th item to Pinecone" + "\n")


for i in range(1, 14):
    addFile(i)
