from langchain_google_genai import GoogleGenerativeAI
from langchain_openai import OpenAI
import asyncio
from prompts import interestSuggestionPrompt2, refiedPromptUisngGPT

prompt = """
give this product description, 
  {
    "data": {
      "product": "Personalized Ice Cream Spoon",
      "description": "- Choose Gift Wrap at checkout to receive Gift Box.\n- New, top quality stainless steel spoons.\n- Custom stamped to order, personalized ice cream spoon.\n- Polished spoon bowl with brushed finish handle.\n- Each letter individually stamped with a steel letter stamp.\n- Letter impressions are filled with non toxic paint, safe to use.\n- Non tarnish.\n-Words will be stamped exactly as spelled on the order.\n- In the font shown in the picture, all uppercase.\n-No quotation marks or emoticons.\n- Oval Teaspoon 6.10\" long x 1.25\" wide, for coffee, tea, desert spoon.\n- Oval Tablespoon 6.75\" long x 1.50\" wide, for cereal, ice cream, dinner spoon.",
      "uniqueAttributes": {
        "Personalized": "The spoon can be custom stamped with any words or name, making it a unique and personal gift for any occasion. This personalization sets it apart from generic ice cream spoons that are mass-produced and lack a personal touch.",
        "High-quality materials": "The spoon is made from top-quality stainless steel, ensuring durability and longevity. This sets it apart from generic spoons that may be made from cheaper materials and may not withstand regular use.",
        "Handcrafted": "Each spoon is individually stamped with a steel letter stamp, giving it a handcrafted quality that is not found in generic spoons. This attention to detail adds to the spoon's charm and makes it a special keepsake.",
        "Non-toxic and safe": "The letter impressions on the spoon are filled with non-toxic paint, making it safe to use for eating. This sets it apart from generic spoons that may use harmful materials that could leach into food."
      },
      "targetAudience": [
        {
          "targetAudience": "Families with children",
          "useCase": "The spoon can be personalized with the names of family members, making it a fun and unique way to enjoy ice cream together."
        },
        {
          "targetAudience": "Couples",
          "useCase": "The spoon can be personalized with a special message or date, making it a romantic and thoughtful gift for anniversaries or Valentine's Day."
        },
        {
          "targetAudience": "Grandparents",
          "useCase": "The spoon can be personalized with the names of grandchildren, making it a cherished keepsake for grandparents to use when they are enjoying ice cream with their loved ones."
        }
      ]
    },
give the a blue print of kind of person that might be interetsed in this

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

generateNuancedTargetAudiancePrompt = """
      "product": "Pendant Ceramic Lamp",
      "description": "This pendant ceramic lamp is a handmade design and a contemporary artwork creation. It is part of the Apilar collection, which is influenced by Spanish ceramics. The lamp has a unique design with nine different shapes that can be stacked on top of each other to create new complex compositions. The lamp also features ceramic prints that are inspired by traditions from different cultures, creating a contemporary cultural collage. The designer is engaged in ongoing research on traditional ceramics as a cultural carrier and is searching for a sense of belonging through the local material culture.",
      "uniqueAttributes": {
        "Handmade": "This piece was created in the innovative studio of the designer-maker Noa Razer, which is located in Tel Aviv, Israel.",
        "Contemporary artwork": "It is part of the Apilar collection, which is a contemporary artwork creation.",
        "Unique design": "The Apilar collection began to take shape during a family roots trip to southern Spain, influenced by the differentiated and unique Spanish ceramics. In this collection, there are nine different shapes, from which all structures of the collection are built.",
        "Cultural collage": "On top of the pieces are ceramic prints, inspired by traditions from different cultures, creating a contemporary cultural collage.",
        "Ongoing research": "The designer is engaged in ongoing research, visual as well as theoretical, focusing on traditional ceramics as a cultural carrier and searching for a sense of belonging through the local material culture."
      }
      given this product description, generate a nuanced target audience for the product. Fill this JSON object
      for example:
      {
        "interests": [
          "Products made in Tel Aviv",
          "comtemporary artwrok part of Apilar collection",
          ""Cultural collage : Ceremic prints inspired from different cultures",
          "Unique design",
          "handmade products"
        ]
      }
      Now do this for product
            "product": "Personalized Vinyl Record Song with Lyrics on Acrylic with Wood Stand",
      "description": "This personalized acrylic song record is a unique and meaningful gift for any occasion. It features your special song, lyrics, and other custom info, making it a truly special keepsake. The modern and eclectic design will fit in with any space in your home, adding a touch of style to your decor. The song record is made from high-quality, guaranteed defect-free, 1/4\" thick acrylic, ensuring its durability and longevity. It comes with a solid wood stand made from oak or walnut, providing a sturdy and stylish base for the song record.",
      "uniqueAttributes": {
        "Personalized": "This song record is personalized with your special song, lyrics, and other custom info, making it a truly unique and meaningful gift.",
        "Modern and eclectic design": "The modern and eclectic design of this song record will fit in with any space in your home, adding a touch of style to your decor.",
        "Custom text": "You can include custom text of your choosing, making this song record even more special and personal.",
        "High-quality materials": "The song record is made from high-quality, guaranteed defect-free, 1/4\" thick acrylic, ensuring its durability and longevity.",
        "Solid wood stand": "The included wood stand is made from solid oak wood or walnut, providing a sturdy and stylish base for the song record."
      }
      only reutrn the JSON object, nothing else
"""

text = """
Imagine you're a social anthropologist studying a fascinating individual. Tell me everything you can learn about them. First extrapolate using the interests mentioned, then combine those multiple interests together and then extrapolate using that.

use this example
{
  "user_description": "Age 25 from montana, recently moved to New York City, likes to play basketball and go to the gym.",
  "output": [
    {
      "reason": "interested in basketball",
      "extrapolation": [
        "sports and physical activities",
        "to be active and social",
      ]
    },
    {
      "reason": "recently moved to New York City",
      "extrapolation": [
        "likes to explore new places",
        "likes to meet new people",
        "open to try new things",
        "showcase cultures of both Montana and New York City"
      ]
    },
    in this one we are combining the two characterstics of the user to get the extrapolation
    {
      "reason": "likes to play basketball and from Montana and New York City",
      "extrapolation": [
        "Supports the New York Knicks",
        "Supports montana grizzlies",
        "Supports other new youk and montana sports teams"
      ]
    },
    {
        "reason": "25 Years old and plays basketball",
        "extrapolation": [
          "likes to go out and have fun",
          "play video games",
          "go to parties"
        ]
    }
    # and more
  ]
}



and return only the answer in JSON format 
{
    "user_description": user_description,
    "output": [
      {
        "reason": "",
        "extrapolation": [

        ]
      },
      {
        "reason": "",
        "extrapolation": [

        ]
      }
    //   as many as needed
      
    ]
  }
make sure to not add any details which cannot be extrapolated from the given input and for every extrapolation provide a reasoning for the same.
only return the JSON object, nothing else
The user_description is as follows :

"""

# User Profile - Occassion, Interests [Given, Extrapolated, Wild Guess], Age
interestSuggestionAgent = """
You are someone who has studied human needs and interests for a long period, you have a deep understanding of human psychology and you can extrapolate the interests, situation they are in currently based on the informatiin provided and even extrapolate other interests,needs and situation based on the given information. You need to provide this analysis in 3 parts 1) Given - This is extracted from the information provided 2) Extrapolated - This is the information that can be extrapolated from the given information 3) Wild Guess - This is the information that is a wild guess which may or may not be accurate but is accurate based on general knowledge which can extrapolated to form the given information taking some assumptions don't just give random guesses.  
You need to provide this information in the JSON format.
-----------------------
Example : 
User : Age 25 from montana, recently moved to New York City, likes to play basketball and go to the gym.
output : 
{
  "Situation" : {
    "Given" : [
      "Recently moved to New York City",
      "Age 25",
      "From Montana"
    ],
    "Extrapolated" : [
      "Adjusting to a fast-paced city lifestyle",
      "Working in a new job or field",
      "Possibly feeling homesick or nostalgic for Montana",
      "Seeking new opportunities and experiences in New York City"
    ],
    "Wild Guess" : [
      "Living in a small apartment in the city",
      "Working in a creative, finance or tech industry for which new York is famous "
    ]
  },
  "Interests" : {
    "Given" : [
      "Playing basketball",
      "Going to the gym"
    ],
    "Extrapolated" : [
      "Staying active and maintaining physical health",
      "Enjoying sports and competition",
      "Possibly interested in other physical activities or team sports"
      "Watching NBA games and following favorite teams/players such as Montana Grizzlies and New York Knicks",
      "Interested in joining a recreational basketball league in the city"
    ],
    "Wild Guess" : [
      "May also enjoy other forms of exercise such as hiking or cycling",
      "May want to visit national parks or outdoor areas near New York City",
    ]
  }
}
-----------------------
Now for this user profile
-----------------------
User : Age 30, recently married, enjoys cooking and gardening in their free time. 

return as many different detailed interests and situation/need they are in as you can in 3 categories - Given, Extrapolated, Wild Guess. IN the given JSON format and don;t limit yourself to the example given above, you can add as many as you can think of.
{
  "Situation" : {
    "Given" : [
      
    ],
    "Extrapolated" : [
      
    ],
    "Wild Guess" : [
      
    ]
  },
  "Interests" : {
    "Given" : [
      
    ],
    "Extrapolated" : [
      
    ],
    "Wild Guess" : [
      
    ]
  }
}
"""

# add a scale to extrapolated and wild guess and try different values till you get the best result

llm = GoogleGenerativeAI(
    model="gemini-1.5-pro-latest",
    google_api_key="AIzaSyAq2iWsgxEXYUPbPnApdDOl0JEa9tvw2Ks",
)  # type: ignore
# llm = OpenAI(openai_api_key="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")  # type: ignore


async def main():
    try:
        result1 = llm.invoke(refiedPromptUisngGPT)
        input2 = (
            "improve upon this, and make it more detailed, reutrn back in exact same format "
            + str(result1)
        )
        print("input 2 begains" + input2)
        print("input 2 ends")

        # result2 = llm.invoke(input2)
        with open("output.txt", "a+") as file:
            file.write(result1)
            file.write(",\n")

        print(result1)
        print("result2")
        # print(result2)``
    except Exception as e:
        print(f"An error occurred: {e}")


asyncio.run(main())
