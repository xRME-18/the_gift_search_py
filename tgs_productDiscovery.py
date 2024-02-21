import json
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from pinecone import Pinecone, ServerlessSpec
from flask import Flask, request
from langchain.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI


from utils import generateRandomStringId

pc = Pinecone()
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
)
model = genai.GenerativeModel(model_name="gemini-pro")
llm = GoogleGenerativeAI(model="gemini-pro")

text = """
Imagine you're a social anthropologist studying a fascinating individual. Tell me everything you can learn about them. First extrapolate using the interests mentioned, then combine those multiple interests together and then extrapolate using that.

use this example
{
  "user_description": "Age 25 from montana, recently moved to New York City, likes to play basketball and go to the gym.",
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
    "user_description": user_description,
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
The user_description is as follows :

"""


refine_user_prompt_template = PromptTemplate.from_template(text)
print(refine_user_prompt_template)


index = pc.Index("tgs-cgp-index")

app = Flask(__name__)


@app.route("/discover", methods=["GET"])
async def addProduct():
    payload = request.get_json()
    # convert data form json to string
    user_prompt = str(payload["user_prompt"])
    metadata = payload["metadata"]

    # LLM_prompt = refine_user_prompt_template.format(user_description=user_prompt)
    LLM_prompt = text + user_prompt
    print(LLM_prompt)

    # Refine user prompt using Google Generative AI
    # refined_prompt = await model.aquery(LLM_prompt)
    refined_prompt = llm.invoke(LLM_prompt)

    print(refined_prompt)

    with open("./LLM_generated_ProductDIscovery.json", "a+") as file:
        file.write(f"{refined_prompt},")

    # Generate embedding using Google Generative AI
    vectors = await embeddings.aembed_documents(str(refined_prompt))
    print(type(vectors))

    query_response = index.query(
        namespace=None,
        vector=vectors,
        top_k=2,
        include_values=True,
        include_metadata=True,
    )
    # print(query_response)

    matches = query_response["matches"]
    productList = []
    for match in matches:
        id = match["id"]
        url = match["metadata"]["url"]
        description = match["metadata"]["description"]
        product = match["metadata"]["product"]

        productList.append((id, url, description, product))

    return productList
