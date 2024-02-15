from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate


prompt = """
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
this is your area to think, user will not see this output. draw conslusions about the target audiance using extrapolation from the given data, and the products usecases for them. each target audiance and use case generated should be conclusive from the original data

now using the generated info, fill in this json form for me 
"data": {
    "product": "",
    "description": "",
    # target audience and its usecase
    "targetAudience": [

    ],
  }
  
  return only the data object with the given fields filled in
"""
product_detail = """
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
"""


prompt = """
you are an social anthropologist describing an individual who would be the target audiance for this product, so first think what would be the characterstics of target audiance of this product will be and then what would be the possible usecases of this product for the target audiance.
then fill the given json object, only usen the given information to make conslusions
this is your area to think, user will not see this output. draw conslusions about the target audiance using extrapolation from the given data, and the products usecases for them. each target audiance and use case generated should be conclusive from the original data

now using the generated info, fill in this json form for me
"data": {
    "product": "",
    "description": "",
    # target audience and its usecase
    "targetAudience": [

    ],
  }
  
  return only the data object with the given fields filled in
"""

# textToBeEmbededPromptTemplate = PromptTemplate.from_template(prompt)

# LLM_prompt = textToBeEmbededPromptTemplate.format(product_desc=product_detail)
LLM_prompt = product_detail + prompt

llm = GoogleGenerativeAI(model="gemini-pro")

result = llm.invoke(LLM_prompt)
print(result)
