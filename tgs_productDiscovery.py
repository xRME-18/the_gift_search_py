from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from pinecone import Pinecone, ServerlessSpec
from flask import Flask, request
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


from utils import generateRandomStringId

pc = Pinecone()
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
)
model = genai.GenerativeModel(model_name="gemini-pro")
llm = ChatGoogleGenerativeAI(model="gemini-pro")

text = """
Imagine you're a social anthropologist studying a fascinating individual: {user_description}. Tell me everything you can learn about their:

Worldview: What are their values and beliefs? How do they see the world and their place in it?
Habits and routines: What does a typical day or week look like for them? What are their hobbies and pursuits outside of their main interests?
Community and connections: Who are the people they surround themselves with? What kind of community do they belong to or aspire to?
Dreams and aspirations: What are their hopes and goals for the future? What challenges do they face and how do they overcome them?
Unexpected quirks and hidden depths: What hidden talents or interests do they possess? What surprising things might someone learn about them upon closer inspection?
make sure to not add any details which cannot be extrapolated from the given input and for every extrapolation provide a reasoning for the same. 
"""


refine_user_prompt_template = PromptTemplate.from_template(text)


index = pc.Index("tgs-cgp-index")

app = Flask(__name__)


@app.route("/discover", methods=["GET"])
async def addProduct():
    payload = request.get_json()
    # convert data form json to string
    user_prompt = str(payload["user_prompt"])
    metadata = payload["metadata"]

    LLM_prompt = refine_user_prompt_template.format(user_description=user_prompt)
    print(LLM_prompt)

    # Refine user prompt using Google Generative AI
    # refined_prompt = await model.aquery(LLM_prompt)
    refined_prompt = llm.invoke(LLM_prompt)

    print(refined_prompt)

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
