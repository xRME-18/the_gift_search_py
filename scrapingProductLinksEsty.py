import requests
from bs4 import BeautifulSoup
import json

url = "https://www.etsy.com/c/home-and-living/home-decor?ref=pagination&plkey=3143cfbf116da656d57ba0de96febe84c9de0ffa%3A956382765&listing_id=956382765&listing_slug=romantic-couple-personalized-resin-tree&explicit=1&page=3"

# HEADERS = {
#     "User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
# }
# response = requests.get(url, headers=HEADERS)


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

# Find all product listings
product_listings = soup.find_all("a", class_="listing-link wt-display-inline-block")

product_listings_links = []

for product in product_listings:
    product_link = product["href"]
    product_listings_links.append(product_link)
print(len(product_listings_links))


product_links = {"links": product_listings_links}

with open("product_links.json3", "w") as file:
    json.dump(product_links, file)
