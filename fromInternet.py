from bs4 import BeautifulSoup
import requests

base_url = "https://www.etsy.com/search?q=handmade+jewelry&page="
# Loop through the first 5 pages of search results
for page in range(1, 6):
    url = base_url + str(page)
    # Send a GET request to the webpage
    response = requests.get(url)
    # Parse the content of the request with BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    # Find all product listings on the page
    listings = soup.find_all("div", class_="v2-listing-card__info")
    # For each listing, extract the URL of the product page
    for listing in listings:
        # The URL is in an ‹a> tag with class 'display-inline-block listing-link'
        product_url = listing.find("a", class_="display-inline-block listing-link")
        # Send a GET request to the product page
        product_response = requests.get(product_url)
        # Parse the content of the product page with BeautifulSoup
        product_soup = BeautifulSoup(product_response.content, "html.parser")
        # Extract the product name, price, and product details
        product_name = product_soup.find("h1", class_="wt-text-body-03").text.str
        price = product_soup.find("p", class_="wt-text-title-03").text.strip()
        product_details = product_soup.find("div", class_="wt-text-body-01").text
