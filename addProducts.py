import json

from addToPinecone import addEmbeddingsToPinecone


# Specify the path to your JSON file
def addfile(numbers):
    file_path = (
        "./finalJSON/Product_Embedding_EstyPersonalisedGiftDescription"
        + str(numbers)
        + ".json"
    )

    # Open the file and load the JSON data
    with open(file_path, "r") as file:
        json_data = json.load(file)

        # Now you can work with the loaded JSON data as a list
        for i, item in enumerate(json_data):
            print(f"Product {i + 1}")
            addEmbeddingsToPinecone(item)
            print("Added {i}th item to Pinecone" + "\n")


for i in range(2, 14):
    addfile(i)
