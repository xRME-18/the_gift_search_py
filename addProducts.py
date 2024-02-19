import json

from addToPinecone import addEmbeddingsToPinecone

# Specify the path to your JSON file
file_path = "./productEmbedding_JSON_list1.json"

# Open the file and load the JSON data
with open(file_path, "r") as file:
    json_data = json.load(file)

    # Now you can work with the loaded JSON data as a list
    for i, item in enumerate(json_data):
        print(f"Product {i + 1}")
        addEmbeddingsToPinecone(item)
        print("Added {i}th item to Pinecone" + "\n")

# addEmbeddingsToPinecone(json_data[0])
