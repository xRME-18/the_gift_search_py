from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from pinecone import Pinecone, ServerlessSpec
from utils import generate_local_embeddings, generateRandomStringId


from utils import generateRandomStringId


pc = Pinecone()
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
)  # type: ignore
model = genai.GenerativeModel(model_name="gemini-pro")
index = pc.Index("tgs-cgp-index")
# Load the tokenizer


def addEmbeddingsToPinecone(payload):
    # convert data form json to string
    data = payload["data"]
    metadata = payload["metadata"]
    metadata["product"] = data["product"]
    metadata["description"] = data["description"]
    data.pop("description")
    data = str(data)

    # Generate embedding using Google Generative AI
    # vectors = embeddings.embed_documents(data)

    vectors = generate_local_embeddings(data)

    pineCodeVectors = []
    # !TODO make sure the metadata size is less then 4096 bytes
    # texts = list(filter(lambda x: len(x) <= 40960, texts))
    # https://github.com/langchain-ai/langchain/issues/3800
    pineCodeVectors.append((metadata["productId"], vectors, metadata))

    # Index the embedding
    if index is not None:
        index.upsert(
            pineCodeVectors,
            namespace="from-GIST-small",
        )
