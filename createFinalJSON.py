import json

from listingGenerator import generateJSONForEmbedding


def createFinalJSON():
    # load json file
    product_details = None
    with open("product_details_list3.json", "r") as file:
        product_details = json.load(file)
    # product_details = [product_details[0]]
    # print(product_details)

    productEmbedding_JSON_list = []

    for i, product in enumerate(product_details):
        print("starting product: ", i)
        productEmbedding_JSON = generateJSONForEmbedding(product)
        productEmbedding_JSON_list.append(productEmbedding_JSON)
        print("finished product: ", i)

    with open("productEmbedding_JSON_list1.json", "w") as file:
        json.dump(productEmbedding_JSON_list, file)


# run the above function
createFinalJSON()
