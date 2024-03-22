from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["cluster0"]

# Define the updated schema
genericProductSchema = {
    "data": {
        "product": str,
        "description": str,
        "uniqueAttributes": [{"attribute": str, "details": str}],
        "targetAudience": [{"target": str, "reasons": str}],
    },
    "metadata": {"url": str, "dateCreated": str, "productId": str},
}


# Create a collection and insert the document
# collection = db["products"]
# collection.insert_one(
#     {
#         "data": {
#             "product": "",
#             "description": "",
#             "uniqueAttributes": [{"attribute": "", "details": ""}],
#             "targetAudience": [{"target": "", "reasons": ""}],
#         },
#         "metadata": {
#             "url": "",
#             "dateCreated": "2024-03-01T10:40:09.309265",
#             "productId": "cfXEFUrkIF",
#         },
#     }
# )
