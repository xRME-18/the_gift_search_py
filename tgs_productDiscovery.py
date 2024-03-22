import json
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from pinecone import Pinecone, ServerlessSpec
from flask import Flask, request
from langchain.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from flask_cors import CORS
from langchain_community.llms import openai
from utils import generate_local_embeddings
from utils import generateRandomStringId
from prompts import interestSuggestionAgent, consolidateInterests

pc = Pinecone()
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
)  # type: ignore
# embeddings = embeddings.openai_langchain_embeddings()

model = genai.GenerativeModel(model_name="gemini-pro")
llm = GoogleGenerativeAI(model="gemini-pro")  # type: ignore

text = """
Imagine you're a social anthropologist studying a fascinating individual. Tell me everything you can learn about them. First extrapolate using the interests mentioned, then combine those multiple interests together and then extrapolate using that.

use this example
{
  "user_Description": "Age 25 from montana, recently moved to New York City, likes to play basketball and go to the gym.",
  "output": [
    {
      "reason": "interested in basketball",
      "extrapolation": [
        "sports and physical activities",
        "to be active and social",
      ]
    },
    {
      "reason": "recently moved to New York City",
      "extrapolation": [
        "likes to explore new places",
        "likes to meet new people",
        "open to try new things",
        "showcase cultures of both Montana and New York City"
      ]
    },
    in this one we are combining the two characterstics of the user to get the extrapolation
    {
      "reason": "likes to play basketball and from Montana and New York City",
      "extrapolation": [
        "Supports the New York Knicks",
        "Supports montana grizzlies",
        "Supports other new youk and montana sports teams"
      ]
    },
    {
        "reason": "25 Years old and plays basketball",
        "extrapolation": [
          "likes to go out and have fun",
          "play video games",
          "go to parties"
        ]
    }
    # and more
  ]
}



and return only the answer in JSON format 
{
    "user_Description": user_Description,
    "output": [
      {
        "reason": "",
        "extrapolation": [

        ]
      },
      {
        "reason": "",
        "extrapolation": [

        ]
      }
    //   as many as needed
      
    ]
  }
make sure to not add any details which cannot be extrapolated from the given input and for every extrapolation provide a reasoning for the same.
only return the JSON object, nothing else
The user_Description is as follows :

"""


refine_user_prompt_template = PromptTemplate.from_template(text)


index = pc.Index("tgs-cgp-index")

app = Flask(__name__)
CORS(app)


@app.route("/discover", methods=["POST"])
async def addProduct():
    payload = request.get_json()
    # convert data form json to string
    user_prompt = str(payload["user_prompt"])

    # use metadata as filter in pinecone query
    metadata = payload["metadata"]

    # LLM_prompt = refine_user_prompt_template.format(user_Description=user_prompt)
    LLM_prompt = interestSuggestionAgent + user_prompt

    # Refine user prompt using Google Generative AI
    # refined_prompt = await model.aquery(LLM_prompt)
    refined_prompt = ""
    user_profile = {}
    try:
        refined_prompt = llm.invoke(LLM_prompt)
        user_profile = json.loads(refined_prompt)
    except Exception as e:
        print(e)

    with open("./LLM_generated_ProductDIscovery.json", "a+") as file:
        file.write(f"{refined_prompt},")

    del user_profile["Interests"]["Given"]
    del user_profile["Situation"]["Given"]
    user_profile_string = json.dumps(user_profile)

    consolidateInterestResult = {}
    try:
        consolidateInterestResult = llm.invoke(
            consolidateInterests + user_profile_string
        )
        consolidateInterestResult = json.loads(consolidateInterestResult)
    except Exception as e:
        print(e)

    # Generate embedding using Google Generative AI
    # vectors = await embeddings.aembed_documents(str(refined_prompt))
    # vectors = generate_local_embeddings(str(refined_prompt))
    # situation_given = user_profile["Situation"]["Given"]
    situation_extrapolated = user_profile["Situation"]["Extrapolated"]
    situation_wild_guess = user_profile["Situation"]["Wild Guess"]

    # interests_given = user_profile["Interests"]["Given"]
    interests_extrapolated = user_profile["Interests"]["Extrapolated"]
    interests_wild_guess = user_profile["Interests"]["Wild Guess"]
    productList = []

    # for i in range(len(situation_given)):
    #     vectors = generate_local_embeddings(situation_given[i])
    #     query_response = index.query(
    #         namespace="genericProduct",
    #         vector=vectors,
    #         top_k=2,
    #         # include_values=True,
    #         include_metadata=True,
    #     )
    #     matches = query_response["matches"]
    #     for match in matches:
    #         id = match["id"]

    #         Description = match["metadata"]["Description"]
    #         product = match["metadata"]["product"]

    #         productList.append(
    #             {
    #                 "interest/situation": situation_given[i],
    #                 "id": id,
    #                 "Description": Description,
    #                 "product": product,
    #             }
    #         )
    for i in range(len(situation_extrapolated)):
        vectors = generate_local_embeddings(situation_extrapolated[i])
        query_response = index.query(
            namespace="genericProduct",
            vector=vectors,
            top_k=2,
            # include_values=True,
            include_metadata=True,
        )
        matches = query_response["matches"]
        for match in matches:
            id = match["id"]

            Description = match["metadata"]["Description"]
            product = match["metadata"]["product"]

            productList.append(
                {
                    "interest/situation": situation_extrapolated[i],
                    "id": id,
                    "Description": Description,
                    "product": product,
                }
            )
    for i in range(len(situation_wild_guess)):
        vectors = generate_local_embeddings(situation_wild_guess[i])
        query_response = index.query(
            namespace="genericProduct",
            vector=vectors,
            top_k=2,
            # include_values=True,
            include_metadata=True,
        )
        matches = query_response["matches"]
        for match in matches:
            id = match["id"]

            Description = match["metadata"]["Description"]
            product = match["metadata"]["product"]
            additionalFeatures = match["metadata"]["additionalFeatures"]

            productList.append(
                {
                    "interest/situation": situation_wild_guess[i],
                    "id": id,
                    "Description": Description,
                    "additionalFeatures": additionalFeatures,
                    "product": product,
                }
            )
    # for i in range(len(interests_given)):
    #     vectors = generate_local_embeddings(interests_given[i])
    #     query_response = index.query(
    #         namespace="genericProduct",
    #         vector=vectors,
    #         top_k=2,
    #         # include_values=True,
    #         include_metadata=True,
    #     )
    #     matches = query_response["matches"]
    #     for match in matches:
    #         id = match["id"]

    #         Description = match["metadata"]["Description"]
    #         product = match["metadata"]["product"]

    #         productList.append(
    #             {
    #                 "interest/situation": interests_given[i],
    #                 "id": id,
    #                 "Description": Description,
    #                 "product": product,
    #             }
    #         )
    for i in range(len(interests_extrapolated)):
        vectors = generate_local_embeddings(interests_extrapolated[i])
        query_response = index.query(
            namespace="genericProduct",
            vector=vectors,
            top_k=2,
            # include_values=True,
            include_metadata=True,
        )
        matches = query_response["matches"]
        for match in matches:
            print(match)
            id = match["id"]
            Description = match["metadata"]["Description"]
            product = match["metadata"]["product"]
            additionalFeatures = match["metadata"]["additionalFeatures"]

            productList.append(
                {
                    "interest/situation": interests_extrapolated[i],
                    "id": id,
                    "additionalFeatures": additionalFeatures,
                    "Description": Description,
                    "product": product,
                }
            )
    for i in range(len(interests_wild_guess)):
        vectors = generate_local_embeddings(interests_wild_guess[i])
        query_response = index.query(
            namespace="genericProducts",
            vector=vectors,
            top_k=2,
            # include_values=True,
            include_metadata=True,
        )
        matches = query_response["matches"]
        for match in matches:
            id = match["id"]
            Description = match["metadata"]["Description"]
            product = match["metadata"]["product"]

            productList.append(
                {
                    "interest/situation": interests_wild_guess[i],
                    "id": id,
                    "Description": Description,
                    "product": product,
                }
            )
    # consolidateInterestResult_string = ""
    # for key in consolidateInterestResult:
    #     consolidateInterestResult_string += consolidateInterestResult[key] + " "
    # vectors = generate_local_embeddings(consolidateInterestResult_string)
    # query_response = index.query(
    #     namespace="genericProduct",
    #     vector=vectors,
    #     top_k=2,
    #     # include_values=True,
    #     include_metadata=True,
    # )
    # matches = query_response["matches"]
    # for match in matches:
    #     id = match["id"]

    #     Description = match["metadata"]["Description"]
    #     product = match["metadata"]["product"]

    #     productList.append(
    #         {
    #             "interest/situation": consolidateInterestResult_string,
    #             "id": id,
    #             "Description": Description,
    #             "product": product,
    #         }
    #     )

    # Write productList to a file
    with open("product_list.jsonl", "a+") as file:
        json.dump(productList, file)

    # print(productList)
    return json.dumps(productList)
