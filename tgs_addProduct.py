from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from pinecone import Pinecone, ServerlessSpec
from flask import Flask, request

from utils import generateRandomStringId


pc = Pinecone()
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
)
model = genai.GenerativeModel(model_name="gemini-pro")


# if "tgs-cgp-index" not in pc.list_indexes():
#     pc.create_index(
#         name="tgs-cgp-index",
#         dimension=768,
#         metric="euclidean",
#         spec=ServerlessSpec(cloud="aws", region="us-west-2"),
# )

index = pc.Index("tgs-cgp-index")

app = Flask(__name__)


@app.route("/addProduct", methods=["POST"])
async def addProduct():
    payload = request.get_json()
    # convert data form json to string
    data = payload["data"]
    metadata = payload["metadata"]
    metadata["product"] = data["product"]
    metadata["description"] = data["description"]
    data = str(data)

    # Generate embedding using Google Generative AI
    vectors = await embeddings.aembed_documents(data)
    print(type(vectors))

    productId = generateRandomStringId()
    metadata["productId"] = productId

    pineCodeVectors = []
    # !TODO make sure the metadata size is less then 4096 bytes
    # texts = list(filter(lambda x: len(x) <= 40960, texts))
    # https://github.com/langchain-ai/langchain/issues/3800
    pineCodeVectors.append((productId, vectors, metadata))

    # Index the embedding
    index.upsert(
        pineCodeVectors,
        namespace=None,
    )

    return "Embedding created successfully"
