import requests
from bs4 import BeautifulSoup
import json

from utils import generateRandomStringId
# import requests_cache


def scrape_file(number):
    product_links = {"links": []}
    # commented so as not to make requests accidentally
    with open("./productLinks/EstyLinks" + str(number) + ".json", "r") as file:
        links = json.load(file)

        for link in links:
            product_links["links"].append(link["href"])

        # print(links[0])
        # href_values = [obj["href"] for obj in file]
        # print(href_values)

    links = product_links["links"]
    # links.map(lambda x: x["href"])

    # print(links)
    # link = "https://www.etsy.com/in-en/listing/999136086/pendant-ceramic-lamp-hanging-lampshade?click_key=325f12948fc651e9fc141aa7ea2fecee40251e0a:999136086&click_sum=62331cd9&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=Pendant+Ceramic+Lamp,+Hanging+Ceiling+Lamp,+Handmade+Design,Printed+Decoration+of+Green+Leave&etp=1&search_preloaded_img=1"

    all_products = []

    with open(
        "./scrappedProductDescription/EstyDetails" + str(number) + ".json",
        "a+",
    ) as file:
        for index, link in enumerate(links):
            # response = requests.get(
            #     url="https://proxy.scrapeops.io/v1/",
            #     params={
            #         "api_key": "a066a2c2-b21d-4960-a83b-82c4b113ba90",
            #         "url": link,
            #         "country": "us",
            #     },
            # )
            print(f"Scraping product {index + 1} of {len(links)}")
            response = requests.get(
                url="https://proxy.scrapeops.io/v1/",
                params={
                    "api_key": "4101ab50-0ac9-4d62-b9a1-85f5ba999041",
                    "url": link,
                    "country": "us",
                },
            )

            # payload = {
            #     "source": "universal_ecommerce",
            #     "url": link,
            #     "geo_location": "United States",
            #     "parse": False,
            # }

            # # Get response.
            # response = requests.request(
            #     "POST",
            #     "https://realtime.oxylabs.io/v1/queries",
            #     auth=("losslessENt", "losslessEnt1234"),
            #     json=payload,
            # )

            # print(response.text)
            # json.dump(response.text, file)
            # file.write(",\n")
            # break

            try:
                soup = BeautifulSoup(response.text, "html.parser")
                # print("Soup created")

                title_elements = soup.find_all(
                    "h1",
                    class_="wt-text-body-01 wt-line-height-tight wt-break-word wt-mt-xs-1",
                )
                title = [title.get_text(strip=True) for title in title_elements][0]
                # print("Title extracted")

                # Extracting descriptions
                description_elements = soup.find_all(
                    "p", class_="wt-text-body-01 wt-break-word"
                )
                description = [
                    description.get_text(strip=True)
                    for description in description_elements
                ][0]
                # print("Description extracted")

                # Extracting reviews
                reviews_elements = soup.find_all(
                    "p",
                    class_="wt-text-truncate--multi-line wt-break-word wt-text-body",
                )
                reviews = [review.get_text(strip=True) for review in reviews_elements]
                # print("Reviews extracted")

                product_details = {
                    "productId": generateRandomStringId(),
                    "url": link,
                    "title": title,
                    "description": description,
                    "reviews": reviews,
                }
                # print(f"Product details: {product_details}")
                json.dump(product_details, file)
                # print("Product details dumped to file")
            except Exception as e:
                print(f"An error occurred while scraping: {str(e)}")
            # all_products.append(product_details)
            # print(f"Product {index + 1} title: {title}")


for number in range(1, 17):
    scrape_file(str(number))
# scrape_file(9)
