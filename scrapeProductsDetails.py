import requests
from bs4 import BeautifulSoup
import json

from utils import generateRandomStringId
# import requests_cache


product_links = {"links": []}

with open("product_links.json", "r") as file:
    links = json.load(file)
    product_links["links"] = links["links"]

links = product_links["links"]
# link = "https://www.etsy.com/in-en/listing/999136086/pendant-ceramic-lamp-hanging-lampshade?click_key=325f12948fc651e9fc141aa7ea2fecee40251e0a:999136086&click_sum=62331cd9&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=Pendant+Ceramic+Lamp,+Hanging+Ceiling+Lamp,+Handmade+Design,Printed+Decoration+of+Green+Leave&etp=1&search_preloaded_img=1"

all_products = []

for index, link in enumerate(links):
    response = requests.get(
        url="https://proxy.scrapeops.io/v1/",
        params={
            "api_key": "a066a2c2-b21d-4960-a83b-82c4b113ba90",
            "url": link,
            "country": "us",
        },
    )

    soup = BeautifulSoup(response.text, "html.parser")

    title_elements = soup.find_all(
        "h1", class_="wt-text-body-01 wt-line-height-tight wt-break-word wt-mt-xs-1"
    )
    title = [title.get_text(strip=True) for title in title_elements][0]

    # Extracting descriptions
    description_elements = soup.find_all("p", class_="wt-text-body-01 wt-break-word")
    description = [
        description.get_text(strip=True) for description in description_elements
    ][0]

    # Extracting reviews
    reviews_elements = soup.find_all(
        "p", class_="wt-text-truncate--multi-line wt-break-word wt-text-body-01"
    )
    reviews = [review.get_text(strip=True) for review in reviews_elements]

    product_details = {
        "productId": generateRandomStringId(),
        "url": link,
        "title": title,
        "description": description,
        "reviews": reviews,
    }
    all_products.append(product_details)
    print(f"Product {index + 1} title: {title}")


# Write the product details to a JSON file
with open("product_details_list.json", "w") as file:
    json.dump(all_products, file)

# with open("product_details.txt", "w") as file:
#     file.write(f"Title: {title}\n")
#     file.write(f"Description: {description}\n")
#     file.write(f"Reviews: {reviews}\n")
