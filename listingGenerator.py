import json
from langchain_google_genai import GoogleGenerativeAI

example_prompt = """
{
    "productId": "HMxVfXrrfJ",
    "title": "Pendant Ceramic Lamp, Hanging Lampshade, Handmade Design, Contemporary Artwork Creation, Unique Light Fixture Gift",
    "description": "Pendant Ceramic Lamp, Hanging Lampshade, Handmade Design, Contemporary Artwork Creation, Unique Light Fixture Gift, Suitable for Living Room Center & Office by Noa RazerThis piece was created in the innovative studio of the designer-maker Noa Razer, which is located in Tel Aviv, Israel, and It is part of the Apilar collection.The Apilar collection ('stack' in Spanish) began to take shape during a family roots trip to southern Spain, influenced by the differentiated and unique Spanish ceramics. In this collection, there are nine different shapes, from which all structures of the collection are built. Countless creation options are formed by stacking the shapes one on top of the other into new complex compositions with spectacular colors.On top of the pieces are ceramic prints, inspired by traditions from different cultures, creating a contemporary cultural collage.The designer is engaged in ongoing research, visual as well as theoretical, focusing on \u200ftraditional ceramics as a cultural carrier and \u200fsearching for a sense of belonging through the local material culture.Color: Green, pink, tealMeasurements:Height\t5.9 inchDiameter of 5.5 inch",
    "reviews": [
        "Amazing, delicate yet sturdy. Beautiful craftsmanship.",
        "Great item and customer service",
        "Soooo gorgeous, they're in my daughter's room. Everyone new to her space notices them and shares how lovely they are. Thank you.",
        "This light is stunning!"
    ]
}

you are an social anthropologist describing an individual who would be the target audiance for this product, so first think what would be the characterstics of target audiance of this product will be and then what would be the possible usecases of this product for the target audiance.
then fill the given json object, only usen the given information to make conslusions
this is your area to think, user will not see this output. draw conslusions about the target audiance using extrapolation from the given data, and the products usecases for them. each target audiance and use case generated should be conclusive from the original data, in the tagret audience section give few sentences of who the target audiance is and how would they use it or how doees it benifit them.

now using the generated info, fill in this json form for me 
"data": {
    "product": "",
    "description": "",
    # target audience and its usecase
    "targetAudience": [
        # example
        {
            "targetAudience": "Art collectors",
            "useCase": "This lamp would be a great addition to any art collection. It is a unique and stylish piece that is sure to be appreciated by art lovers."
        },
        {
            "targetAudience": "Interior designers",
            "useCase": "This lamp would be a great way to add a touch of contemporary style to any home or office. It is a versatile piece that can be used in a variety of settings."
        },
        {
            "targetAudience": "Homeowners who are looking for a unique and stylish lighting fixture",
            "useCase": "This lamp would be a great way to add a touch of personality to any home. It is a unique and stylish piece that is sure to make a statement."
        }

    ],
  }
  
  return only the data object with the given fields filled in
"""

product_detail_json = {
    "productId": "HMxVfXrrfJ",
    "title": "Pendant Ceramic Lamp, Hanging Lampshade, Handmade Design, Contemporary Artwork Creation, Unique Light Fixture Gift",
    "description": "Pendant Ceramic Lamp, Hanging Lampshade, Handmade Design, Contemporary Artwork Creation, Unique Light Fixture Gift, Suitable for Living Room Center & Office by Noa RazerThis piece was created in the innovative studio of the designer-maker Noa Razer, which is located in Tel Aviv, Israel, and It is part of the Apilar collection.The Apilar collection ('stack' in Spanish) began to take shape during a family roots trip to southern Spain, influenced by the differentiated and unique Spanish ceramics. In this collection, there are nine different shapes, from which all structures of the collection are built. Countless creation options are formed by stacking the shapes one on top of the other into new complex compositions with spectacular colors.On top of the pieces are ceramic prints, inspired by traditions from different cultures, creating a contemporary cultural collage.The designer is engaged in ongoing research, visual as well as theoretical, focusing on \u200ftraditional ceramics as a cultural carrier and \u200fsearching for a sense of belonging through the local material culture.Color: Green, pink, tealMeasurements:Height\t5.9 inchDiameter of 5.5 inch",
    "reviews": [
        "Amazing, delicate yet sturdy. Beautiful craftsmanship.",
        "Great item and customer service",
        "Soooo gorgeous, they're in my daughter's room. Everyone new to her space notices them and shares how lovely they are. Thank you.",
        "This light is stunning!",
    ],
}


product_detail2_json = {
    "productId": "ZrURmqgcqX",
    "title": "Linen Pillowcase. Linen Pure Pillowcase. Linen Pillow Cover King, Queen, Standard, Euro sizes. Cappuccino linen pillowcover",
    "description": 'Pure 100% Linen pillow cover will provide you maximum comfort.Because of linen\'s natural qualities, you will feel better and sleep deeper.- Price includes 1 Pillowcase- Pillowcase closure type - envelope;- Color: Almon- 100%  Extra Soft Linen ;- Fabric is: Oeko Tex 100 certified;- Made in Lithuania;Match it with almond sheets:https://www.etsy.com/listing/1110228783/linen-sheet-set-2-pillows-in-white-color?click_key=2a2aec771cf355711397c8539c706045b93a164a%3A1110228783&click_sum=fab2cb5a&ga_search_query=sheet%2Bset&ref=shop_items_search_10&frs=1&crt=1&variation1=2319224371And Beige duvet cover:https://www.etsy.com/listing/1071423946/linen-duvet-cover-in-beige-washed-linen?click_key=b88991db21dcd007eb5748e547ab74cc709bf561%3A1071423946&click_sum=5503be5b&ref=shop_home_active_10&frs=1\ud83d\udc8cSIZE CHART:US Standard 20x26"US Queen 20x30"US King 20x36"US Body 20x54"US Boudoir 12x16"US Deco 18x18"EU Deco Small 30x40 cmEU Deco Square 40x40 cmEU Standard 50x70 cmEU IKEA 50x60 cmEU Square 65x65 cmUK Standard 20x30"UK Large Square 26x26"DE Standard 40x80 cmDE King 80x80 cmCustom sizes available - write us a message to find out more.The actual colours may vary slightly because every computer monitor has a different capability to display colours.\ud83d\udc8c  CARE GUIDE:- Wash at or below 60 C/140F;- Do not bleach;- Tumble dry on low heat;- Iron on low heat;- Do not dry clean.\u2708\ufe0f SHIPPING:We ship worldwide:- Standard Priority mail from Lithuania: this shipping method usually takes 5-15 business days to Europe and 9-21 business days to overseas (USA, Australia, New Zealand).- Express. It takes 2-4 business days worldwide. IMPORTANT: If you choose the express shipping method, please write down your phone number in the note section, it helps to avoid delivery problems.',
    "reviews": [
        "Really happy with the linen throw blanket. It's quickly becoming the new favorite around the house.",
        "Beautiful quality and just as described.",
        "Lovely! Love the color, high quality.",
        "Love it -- such nice quality",
    ],
}


targetAudiancePrompt = """
you are an social anthropologist describing an individual who would be the target audiance for this product, so first think what would be the characterstics of target audiance of this product will be and then what would be the possible usecases of this product for the target audiance.
then fill the given json object, only usen the given information to make conslusions
this is your area to think, user will not see this output. draw conslusions about the target audiance using extrapolation from the given data, and the products usecases for them. each target audiance and use case generated should be conclusive from the original data

now using the generated info, fill in this json form for me
"targetAudience": [
    {
        "targetAudience": "",
        "useCase": ""
    },
    {
        "targetAudience": "",
        "useCase": ""
    },
    {
        "targetAudience": "",
        "useCase": ""
    }
    # at lest 3 target audiance and use cases, use more if the product is widely applicable

    ],
  
  return only the data object with the given fields filled in and only return exactly this object
"""

productDescriptionPrompt = """
for product description analyse the given data and draw conslusions about the product in few sentences, do not miss any information reagrding product description from the given data and do not add any additional information that was not provided
fill in the given format
{
    "product": "",
    "description": "",
}
"""


def generateJSONForEmbedding(product_detail_json):
    # remove url key parameter from product_detail_json
    # convert to json
    # product_detail_json = json.loads(product_detail_json)

    product_detail_json.pop("url", None)
    # print(product_detail_json)
    # print(type(product_detail_json))

    # return product_detail_json

    json_string = str(product_detail_json)

    final_promptProductDescription = json_string + productDescriptionPrompt
    final_promptTargetAudiance = json_string + targetAudiancePrompt

    llm = GoogleGenerativeAI(model="gemini-pro")

    result1 = None
    for _ in range(5):
        result1 = llm.invoke(final_promptProductDescription)
        try:
            print("result1")
            print(result1)
            print("\n\n")
            result1 = json.loads(result1)
            break
        except json.JSONDecodeError:
            print("JSON is not in the correct format.")
    else:
        raise ValueError("Converting to JSON failed")

    result2 = None
    for _ in range(5):
        result2 = llm.invoke(final_promptTargetAudiance)
        try:
            print("result2")
            print(result2)
            print("\n\n")
            result2 = json.loads(result2)
            break
        except json.JSONDecodeError:
            print("JSON is not in the correct format.")
    else:
        raise ValueError("Converting to JSON failed")

    # verify if its correct foramt and keep repeting until its correct

    final_data = {}

    final_data["data"] = {
        "product": result1["product"],
        "description": result1["description"],
        "targetAudience": result2["targetAudience"],
    }

    return final_data


# json_string = str(product_detail2_json)

# final_promptProductDescription = json_string + productDescriptionPrompt
# final_promptTargetAudiance = json_string + targetAudiancePrompt

# llm = GoogleGenerativeAI(model="gemini-pro")

# result1 = llm.invoke(final_promptProductDescription)
# result2 = llm.invoke(final_promptTargetAudiance)

# # convert string back to json
# result1 = json.loads(result1)
# result2 = json.loads(result2)

# # verify if its correct foramt and keep repeting until its correct

# final_data = {}

# final_data["data"] = {
#     "product": result1["product"],
#     "description": result1["description"],
#     "targetAudience": result2["targetAudience"],
# }

# print(json.dumps(final_data, indent=2))

# print(result1 + "\n\n" + result2)
