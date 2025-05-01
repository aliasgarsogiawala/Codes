import requests
from bs4 import BeautifulSoup

def BDGPrice(casnumber):
    url = f"https://bdg.co.nz/?s={casnumber}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    grid = soup.find("div", class_="post-title")
    if grid is None:
        print("NA")
    else:
        productlink = grid.find("a")["href"]
        response2 = requests.get(productlink)
        soup2 = BeautifulSoup(response2.content, "html.parser")
        finalgrid = soup2.find("form", class_="variations_form cart")
        options = finalgrid.find_all("option")
        prices = soup2.find_all("span", class_="woocommerce-Price-amount amount")
        quantities = [option.text.strip() for option in options if "Choose" not in option.text.strip()]
        prices = [float(price.text.replace(",", "").replace("$", "")) for price in prices]
        results = [{"quantity": quantity, "price":price} for quantity, price in zip(quantities, prices)]
        print(results)
BDGPrice("70020-54-1")
