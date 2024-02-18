import json

from listingGenerator import generateJSONForEmbedding


def createEmbeddings():
    # load json file
    product_details = None
    with open("product_details_list.json", "r") as file:
        product_details = json.load(file)
    product_details = [product_details[0]]
    # print(product_details)

    productEmbedding_JSON_list = []

    for product in product_details:
        productEmbedding_JSON = generateJSONForEmbedding(product)
        productEmbedding_JSON_list.append(productEmbedding_JSON)

    with open("productEmbedding_JSON_list.json", "w") as file:
        json.dump(productEmbedding_JSON_list, file)


# run the above function
createEmbeddings()