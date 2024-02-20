import random
import string

from pinecone import Pinecone, ServerlessSpec


def generateRandomStringId() -> str:
    randomChars = str.join(string.ascii_letters, string.digits)
    result = ""
    for _ in range(10):
        result += random.choice(randomChars)
    return result


def deletePineconeNamespace(namespace: str):
    pc = Pinecone()
    index = pc.Index("tgs-cgp-index")
    # for deleting namespaces
    index.delete(delete_all=True, namespace=namespace)
