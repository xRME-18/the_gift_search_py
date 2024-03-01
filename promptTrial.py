from langchain_google_genai import GoogleGenerativeAI
from langchain_openai import OpenAI

prompt = """
give this product description, 
    "data": {
      "product": "Round Address Sign, Geometric Address Sign, Round House Numbers, Modern Address Plaque, Custom Address Sign, House Number Plaque",
      "description": "Geometric carved design with acrylic house numbers, perfect modern piece for your home address sign. Great housewarming gifts, realtor closing gifts, or to spruce up your front porch or door decor.\n\nTo order: \n- Choose your size\n- Note your text color\n- Note your background paint or stain color choice in the personalization area.\n\nComes with a sawtooth hanger to hang.",
      "targetAudience": [
        {
          "targetAudience": "Homeowners looking to upgrade their address sign with a stylish and modern option",
          "useCase": "To display their house number prominently and enhance the aesthetic appeal of their home's exterior"
        },
        {
          "targetAudience": "Realtors seeking unique and thoughtful closing gifts for their clients",
          "useCase": "To provide a personalized and practical present that will be cherished by new homeowners"
        },
        {
          "targetAudience": "Individuals seeking decorative accents for their front porch or door",
          "useCase": "To add a touch of modern design and personalization to their outdoor space"
        }
      ]
    },
what differenciates it form its generic counterpart, return the output as a JSON obejct
example : 
"data": { "product": "TerraCotta Lamp Hanging Light Fixture", "description": "Give your home a boost of warmth and a homely feel with a delicate natural terracotta lamp.\nMade by hand in a small boutique studio in Tel Aviv\nAll necessary fitting parts are included.\nTechnical:\nLamp holder: E27\nTransparent cable : 150 cm / 60 inches\nCeiling rose: 10 cm / 4 inches\nEnergy-saving LED light bulbs are recommended. We prefer the Edison Vintage style Bulb.\nVoltage 110V-250V | 25 to 40W max\nThis piece is part of the Apilar collection.\nThe Apilar collection (Stack in Spanish) began to take shape during a family roots trip to southern Spain, influenced by the Differentiated and unique Spanish ceramics. In this collection, there are nine different shapes, from which all structures of the collection are built. Countless of creation options are formed by stacking the shapes one on top of the other into a new complex with spectacular colors.\nPlease note that this object is handmade, and each piece is unique.\nThis object can be ordered in various colors and prints, talk to us for more info.", "targetAudience": [ { "targetAudience": "Homeowners and renters looking to add a touch of warmth and homeliness to their living spaces.", "useCase": "Using the lamp to create a cozy and inviting atmosphere in living rooms, bedrooms, or dining areas." }, { "targetAudience": "Interior designers and decorators seeking unique and handmade lighting solutions for their clients.", "useCase": "Incorporating the lamp into eclectic or bohemian-style interiors, or as a statement piece in minimalist spaces." }, { "targetAudience": "Individuals interested in sustainable and eco-friendly home decor.", "useCase": "Using the lamp as a durable and energy-efficient lighting option that complements their environmentally conscious lifestyle." }
{
    "Handmade" : "This lamp is made by hand in a small boutique studio in Tel Aviv, making each piece unique. This adds a personal touch and artisanal quality that cannot be replicated by mass-produced items.",
    "Natural materials" : "The lamp is made from natural terracotta, giving it a delicate and earthy aesthetic. This sets it apart from generic lamps made from artificial materials",
    "Unique design" : "The Apilar collection, of which this lamp is a part, is inspired by Spanish ceramics and features nine different shapes that can be stacked together to create a variety of designs. This offers a level of creativity and customization that is not found in most generic lamps.",
    "Energy-efficient" : "The lamp is designed to use energy-saving LED light bulbs, making it a more environmentally friendly and cost-effective lighting option.",
    "Versatility" : "The lamp can be used in various settings, from cozy living rooms to minimalist spaces, and can be ordered in different colors and prints to suit individual preferences. This versatility sets it apart from generic lamps that may have a limited range of options."
}
"""

prompt2 = """
give this product description, 
  {
    "title": "Vintage Boucle armchair and ottoman set, Teddy armchair, Handmade Sherpa chair mid century set, small comfy armchair for living room",
    "description": "Vintage Boucle armchair and ottoman set, Teddy armchair, Handmade furniture Sherpa chair  bring a 60's Furniture feel into your home with this solid wood Mid century Armchair Upholstered in boucle teddy soft fabricOur Mid century armchair is made from solid wood and upholstered with brown faux leather.\u2692 All furniture is handmade in our shop!Armchairs can be upholstered in another fabric or stained in another color, contact me for more info\u27a4 **note for NON-EU buyers - please be aware of possible import fees and taxes, these are calculated additionally when the items are sent and these fees are collected by the delivery company and paid on your behalf to your government. The amount of these fees varies in every non-EU country.*** We are sending from Croatia which is a part of the EU - for EU buyers there are no additional fees *\u27a4 Check out my shop for more Mid Century Vintage Furniture \u27a4https://www.etsy.com/shop/RetroDesignCRODimensions:\u2022 Overall height: 74 Centimeters / 29.6 inches\u2022 Overall width: 63 Centimeters / 25.2 inches\u2022 Overall depth: 70 Centimeters / 28 inches\u2022 Seat height: 40 Centimeters / 16 inches\u2022 Seat width: 50 Centimeters / 20 inches\u2022 Seat depth: 50 Centimeters / 20 inchesMaterials:\u2022 Stained Solid Beech Wood\u2022 Boucle teddy fabric\u2022 High quality furniture foam density 30*simple assembly required instructions included",
    "reviews": [
      "Lovely chair, exactly what we wanted",
      "Very good quality armchair that meets our expectations.\nThe follow-up is top notch: thank you Marija!",
      "Very nice armchair! Comfortable and very pretty",
      "The armchair is beautiful, completely in line with the photos and our expectations. The curls are very soft and the seat is comfortable, especially with the footrest.\nVery good responsiveness of the saleswoman and good follow-up. The delays were a little long to receive it, but everything was in accordance with what had been announced."
    ]
  },
what differenciates it form its generic counterpart, return the output as a JSON obejct
description : 
{ "product": "TerraCotta Lamp Hanging Light Fixture", "description": "Give your home a boost of warmth and a homely feel with a delicate natural terracotta lamp.\nMade by hand in a small boutique studio in Tel Aviv\nAll necessary fitting parts are included.\nTechnical:\nLamp holder: E27\nTransparent cable : 150 cm / 60 inches\nCeiling rose: 10 cm / 4 inches\nEnergy-saving LED light bulbs are recommended. We prefer the Edison Vintage style Bulb.\nVoltage 110V-250V | 25 to 40W max\nThis piece is part of the Apilar collection.\nThe Apilar collection (Stack in Spanish) began to take shape during a family roots trip to southern Spain, influenced by the Differentiated and unique Spanish ceramics. In this collection, there are nine different shapes, from which all structures of the collection are built. Countless of creation options are formed by stacking the shapes one on top of the other into a new complex with spectacular colors.\nPlease note that this object is handmade, and each piece is unique.\nThis object can be ordered in various colors and prints, talk to us for more info.", "targetAudience": [ { "targetAudience": "Homeowners and renters looking to add a touch of warmth and homeliness to their living spaces.", "useCase": "Using the lamp to create a cozy and inviting atmosphere in living rooms, bedrooms, or dining areas." }, { "targetAudience": "Interior designers and decorators seeking unique and handmade lighting solutions for their clients.", "useCase": "Incorporating the lamp into eclectic or bohemian-style interiors, or as a statement piece in minimalist spaces." }, { "targetAudience": "Individuals interested in sustainable and eco-friendly home decor.", "useCase": "Using the lamp as a durable and energy-efficient lighting option that complements their environmentally conscious lifestyle." }
output :
{
    "Handmade" : "This lamp is made by hand in a small boutique studio in Tel Aviv, making each piece unique. This adds a personal touch and artisanal quality that cannot be replicated by mass-produced items.",
    "Natural materials" : "The lamp is made from natural terracotta, giving it a delicate and earthy aesthetic. This sets it apart from generic lamps made from artificial materials",
    "Unique design" : "The Apilar collection, of which this lamp is a part, is inspired by Spanish ceramics and features nine different shapes that can be stacked together to create a variety of designs. This offers a level of creativity and customization that is not found in most generic lamps.",
    "Energy-efficient" : "The lamp is designed to use energy-saving LED light bulbs, making it a more environmentally friendly and cost-effective lighting option.",
    "Versatility" : "The lamp can be used in various settings, from cozy living rooms to minimalist spaces, and can be ordered in different colors and prints to suit individual preferences. This versatility sets it apart from generic lamps that may have a limited range of options."
}
"""


# llm = GoogleGenerativeAI(model="gemini-pro")
llm = OpenAI(openai_api_key="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")
try:
    result1 = llm.invoke(prompt2)
    print(result1)
except Exception as e:
    print(f"An error occurred: {e}")
