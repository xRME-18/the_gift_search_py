import json

from listingGenerator import generateJSONForEmbedding


def createFinalJSON(number):
    # load json file
    product_details = None
    with open(
        "./scrappedProductDescription/EstyPersonalisedGiftDescription"
        + str(number)
        + ".json",
        "r",
    ) as file:
        product_details = json.load(file)
    # product_details = [product_details[0]]
    # print(product_details)

    productEmbedding_JSON_list = []

    with open(
        "./finalJSON/Product_Embedding_EstyPersonalisedGiftDescription"
        + str(number)
        + ".json",
        "a+",
    ) as file:
        for i, product in enumerate(product_details):
            print("starting product: ", i)
            productEmbedding_JSON = generateJSONForEmbedding(product)
            productEmbedding_JSON_list.append(productEmbedding_JSON)
            print("finished product: ", i)
            json.dump(productEmbedding_JSON, file)
            file.write(",\n")  # Add a new line after each JSON object


# run the above function
# for number in range(7, 14):
#     createFinalJSON(number)
