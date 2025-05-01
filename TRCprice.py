import requests
from bs4 import BeautifulSoup
def TRCPrice(catnumber):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3 Edge/16.16299'
    }
    url = f"https://www.trc-canada.com/product-detail/?{catnumber}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content,"html.parser")
    grid=soup.find("div",class_="row")
    image=grid.find("div",id="productImage")
    print(image)
TRCPrice("S210002")
