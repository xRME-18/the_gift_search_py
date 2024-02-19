from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from pinecone import Pinecone, ServerlessSpec

from utils import generateRandomStringId


pc = Pinecone()
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
)
model = genai.GenerativeModel(model_name="gemini-pro")
index = pc.Index("tgs-cgp-index")


def addEmbeddingsToPinecone(payload):
    # convert data form json to string
    data = payload["data"]
    metadata = payload["metadata"]
    metadata["product"] = data["product"]
    metadata["description"] = data["description"]
    data = str(data)

    # Generate embedding using Google Generative AI
    vectors = embeddings.embed_documents(data)
    print(type(vectors))

    pineCodeVectors = []
    # !TODO make sure the metadata size is less then 4096 bytes
    # texts = list(filter(lambda x: len(x) <= 40960, texts))
    # https://github.com/langchain-ai/langchain/issues/3800
    pineCodeVectors.append((metadata["productId"], vectors, metadata))

    # Index the embedding
    index.upsert(
        pineCodeVectors,
        namespace=None,
    )
