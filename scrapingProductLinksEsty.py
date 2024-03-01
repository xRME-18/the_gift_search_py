import requests
from bs4 import BeautifulSoup
import json

# url = "https://www.etsy.com/c/home-and-living/home-decor?ref=pagination&plkey=3143cfbf116da656d57ba0de96febe84c9de0ffa%3A956382765&listing_id=956382765&listing_slug=romantic-couple-personalized-resin-tree&explicit=1&page=3"
# personalised GIfts
# url = "https://www.etsy.com/search?q=personalized+gift&anchor_listing_id=1454996909&ref=hp_bubbles_Spring24&mosv=sese&moci=1226894514292&mosi=1238550269208&is_merch_library=true"
# page 2
# url = "https://www.etsy.com/search?q=personalized+gift&anchor_listing_id=1454996909&ref=pagination&mosv=sese&moci=1226894514292&mosi=1238550269208&is_merch_library=true&page=2"
# Gifts for her
# url = "https://www.etsy.com/search?is_merch_library=true&mosv=sese&moci=1185730867767&mosi=1191950140625&q=personalized+gifts+for+women&ref=gifting_seemore&page=1"
url = "https://www.etsy.com/search?is_merch_library=true&is_best_seller=true&mosv=sese&moci=1166700788460&mosi=1166702706712&q=personalized+gift&ref=gifting_seemore&page=2"


response = requests.get(
    url="https://proxy.scrapeops.io/v1/",
    params={
        "api_key": "a066a2c2-b21d-4960-a83b-82c4b113ba90",
        "url": url,
        "country": "us",
    },
)

# print("Response Body: ", response.content)
print(f"Response status code: {response.status_code}")
print(f"Response content: {response.content}")
soup = BeautifulSoup(response.text, "html.parser")

# Write HTML to a file
with open("scraped_html.html", "w") as file:
    file.write(soup.prettify())

# Find all product listings
product_listings = soup.find_all("a", class_="listing-link wt-display-inline-block")

product_listings_links = []

for product in product_listings:
    product_link = product["href"]
    product_listings_links.append(product_link)
print(len(product_listings_links))


product_links = {"links": product_listings_links}

with open("product_links_personalised_gifts.json", "w") as file:
    json.dump(product_links, file)
