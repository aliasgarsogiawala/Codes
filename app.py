import requests
from bs4 import BeautifulSoup
def TRCPrice(catnumber):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3 Edge/16.16299'
    }
    url = f"https://www.trc-canada.com/product-detail/?{catnumber}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content,"html.parser")
    grid = soup.find("div", class_="productContainer")
   
    product_link = grid.find("a")["href"]
    full_url = "https://www.trc-canada.com" + product_link
    response2 = requests.get(full_url, headers=headers)
    soup2 = BeautifulSoup(response2.content, "html.parser")
    grid2 = soup2.find("table", id="orderProductTable")
    print(grid2)
TRCPrice("6109-70-2")
