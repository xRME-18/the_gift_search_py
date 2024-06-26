import json
import datetime
from langchain_google_genai import GoogleGenerativeAI
from langchain_openai import OpenAI


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
    "description": ""
}
"""

productDescriptionPrompt2 = """
Analyse the given text and draw conslusion for what the product is and its detailed description, do not miss any information which describes the product and do not add any additional information that was not provided
Take time to think, this will not be seen by the user.
Now using the generated info, fill in this json form
{
    "product": "",
    "description": ""
}
The output should be exactly like this, and the added info should be in a human readable format, remove all the html and other tags 
"""

targetAudiancePrompt2 = """
the above information givees you title, description and reviews of a particular product and You are a social anthropologist. To identify the ideal target audience for this product, please follow these steps:

1. Product Analysis:
Carefully examine the product's features and potential benefits. [Before starting, you'll need a detailed product description.]
Ask yourself: What problems does this product solve? How might it improve someone's life?

2. Target Audience Profiling:
Based on the product analysis, brainstorm characteristics of individuals who would likely find this product valuable.
Consider: Age, occupation, lifestyle, interests, pain points, and technological proficiency.

3. Use Case Development:
Outline specific scenarios where the target audience would use this product.
Explain how the product's features directly address the needs or desires of the target audience in each scenario.
Important: Ensure your conclusions about the target audience and use cases are logically derived from the product's core attributes.
 
then fill the given json object, only usen the given information to make conslusions
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
]
only return the JSON object, nothing else

"""

uniqueAttributesPrompt = """
give this product description, 
what differenciates it form its generic counterpart, return the output as a JSON obejct
example:
description : 
{ "product": "TerraCotta Lamp Hanging Light Fixture", "description": "Give your home a boost of warmth and a homely feel with a delicate natural terracotta lamp.\nMade by hand in a small boutique studio in Tel Aviv\nAll necessary fitting parts are included.\nTechnical:\nLamp holder: E27\nTransparent cable : 150 cm / 60 inches\nCeiling rose: 10 cm / 4 inches\nEnergy-saving LED light bulbs are recommended. We prefer the Edison Vintage style Bulb.\nVoltage 110V-250V | 25 to 40W max\nThis piece is part of the Apilar collection.\nThe Apilar collection (Stack in Spanish) began to take shape during a family roots trip to southern Spain, influenced by the Differentiated and unique Spanish ceramics. In this collection, there are nine different shapes, from which all structures of the collection are built. Countless of creation options are formed by stacking the shapes one on top of the other into a new complex with spectacular colors.\nPlease note that this object is handmade, and each piece is unique.\nThis object can be ordered in various colors and prints, talk to us for more info.", "targetAudience": [ { "targetAudience": "Homeowners and renters looking to add a touch of warmth and homeliness to their living spaces.", "useCase": "Using the lamp to create a cozy and inviting atmosphere in living rooms, bedrooms, or dining areas." }, { "targetAudience": "Interior designers and decorators seeking unique and handmade lighting solutions for their clients.", "useCase": "Incorporating the lamp into eclectic or bohemian-style interiors, or as a statement piece in minimalist spaces." }, { "targetAudience": "Individuals interested in sustainable and eco-friendly home decor.", "useCase": "Using the lamp as a durable and energy-efficient lighting option that complements their environmentally conscious lifestyle." }
output :
{
    "uniqueAttributes": {
        "Handmade": "This lamp is made by hand in a small boutique studio in Tel Aviv, making each piece unique. This adds a personal touch and artisanal quality that cannot be replicated by mass-produced items.",
        "Natural materials": "The lamp is made from natural terracotta, giving it a delicate and earthy aesthetic. This sets it apart from generic lamps made from artificial materials",
        "Unique design": "The Apilar collection, of which this lamp is a part, is inspired by Spanish ceramics and features nine different shapes that can be stacked together to create a variety of designs. This offers a level of creativity and customization that is not found in most generic lamps.",
        "Energy-efficient": "The lamp is designed to use energy-saving LED light bulbs, making it a more environmentally friendly and cost-effective lighting option.",
        "Versatility": "The lamp can be used in various settings, from cozy living rooms to minimalist spaces, and can be ordered in different colors and prints to suit individual preferences. This versatility sets it apart from generic lamps that may have a limited range of options."
    }
}
"""


def generateJSONForEmbedding(product_detail_json):
    productURL = product_detail_json["url"]
    product_detail_json.pop("url", None)

    json_string = str(product_detail_json)

    final_promptUniqueAttributes = json_string + uniqueAttributesPrompt

    llm = GoogleGenerativeAI(model="gemini-pro")
    # llm = OpenAI(openai_api_key="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")

    result0 = None
    for _ in range(5):
        try:
            result0 = llm.invoke(final_promptUniqueAttributes)
            print("result0")
            print(result0)
            print("\n\n")
            result0 = json.loads(result0)
            if "uniqueAttributes" not in result0 not in result0:
                raise ValueError("uniqueAttributes are required")
            break
        except json.JSONDecodeError:
            print("JSON is not in the correct format.")
        except ValueError as e:
            print(e)
    else:
        raise ValueError("Converting to JSON failed")

    final_promptProductDescription = (
        json_string
        + json.dumps(result0["uniqueAttributes"])
        + productDescriptionPrompt2
    )
    final_promptTargetAudiance = (
        json_string + json.dumps(result0["uniqueAttributes"]) + targetAudiancePrompt2
    )

    result1 = None
    for _ in range(5):
        try:
            result1 = llm.invoke(final_promptProductDescription)
            print("result1")
            print(result1)
            print("\n\n")
            result1 = json.loads(result1)
            if "product" not in result1 or "description" not in result1:
                raise ValueError("product and description are required")
            break
        except json.JSONDecodeError:
            print("JSON is not in the correct format.")
        except ValueError as e:
            print(e)
    else:
        raise ValueError("Converting to JSON failed")

    result2 = None
    for _ in range(5):
        try:
            result2 = llm.invoke(final_promptTargetAudiance)
            print("result2")
            print(result2)
            print("\n\n")
            result2 = json.loads(result2)
            if "targetAudience" not in result2:
                raise ValueError("targetAudience is required")
            targetAudience = result2["targetAudience"]
            for audience in targetAudience:
                if "targetAudience" not in audience or "useCase" not in audience:
                    raise ValueError("targetAudience and useCase are required")
            break
        except json.JSONDecodeError:
            print("JSON is not in the correct format.")
        except ValueError as e:
            print(e)
    else:
        raise ValueError("Converting to JSON failed")

    return {
        "data": {
            "product": result1["product"],
            "description": result1["description"],
            "uniqueAttributes": result0["uniqueAttributes"],
            "targetAudience": result2["targetAudience"],
        },
        "metadata": {
            "url": productURL,
            "dateCreated": datetime.datetime.now().isoformat(),
            "productId": product_detail_json["productId"],
        },
    }
