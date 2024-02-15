import requests
from bs4 import BeautifulSoup
import json

url = "https://www.etsy.com/c/home-and-living/home-decor?ref=cat_breadcrumb&plkey=3143cfbf116da656d57ba0de96febe84c9de0ffa%3A956382765&listing_id=956382765&listing_slug=romantic-couple-personalized-resin-tree&explicit=1"

# HEADERS = {
#     "User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
# }
# response = requests.get(url, headers=HEADERS)


response = requests.get(
    url="https://proxy.scrapeops.io/v1/",
    params={
        "api_key": "a066a2c2-b21d-4960-a83b-82c4b113ba90",
        "url": "https://www.etsy.com/c/home-and-living/home-decor?ref=cat_breadcrumb&plkey=3143cfbf116da656d57ba0de96febe84c9de0ffa%3A956382765&listing_id=956382765&listing_slug=romantic-couple-personalized-resin-tree&explicit=1",
        "country": "us",
    },
)

# print("Response Body: ", response.content)
print(f"Response status code: {response.status_code}")
print(f"Response content: {response.content}")
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

# Find all product listings
product_listings = soup.find_all("a", class_="listing-link wt-display-inline-block")

product_listings_links = []

for product in product_listings:
    # Get product title
    # product_link = product.find("a", class_="listing-link")["href"]
    product_link = product["href"]
    product_listings_links.append(product_link)
    # print(f"Product Link: {product_link}")
    # product_listings_links.append(product_link)
print(len(product_listings_links))
# Store product_listing_links in a file as an array
product_links = {"links": product_listings_links}

with open("product_links.json", "w") as file:
    json.dump(product_links, file)

# Open the file and read the product links


# open all links to find additional details

# for link in product_listings_links:
#     response = requests.get(link)
#     soup = BeautifulSoup(response.text, "html.parser")
#     print(soup.prettify())
#     product_description = soup.find("p", class_="wt-text-body-03 wt-break-word").text
#     print(f"Product Description: {product_description}")
#     product_name = soup.find("h1", class_="wt-text-title-01 wt-mb-xs-2").text
#     print(f"Product Name: {product_name}")
#     product_price = soup.find("p", class_="wt-text-title-03 wt-mr-xs-2").text
#     print(f"Product Price: {product_price}")
#     product_image = soup.find(
#         "img",
#         class_="wt-max-width-full wt-horizontal-center wt-vertical-center carousel-image wt-rounded",
#     )["src"]
#     print(f"Product Image: {product_image}")
#     print("\n\n")
