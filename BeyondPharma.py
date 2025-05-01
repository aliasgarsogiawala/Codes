import requests
from bs4 import BeautifulSoup

def BeyondPharma(name):
    url = f"http://www.beyond-pharma.com/index.php?m=home&c=Search&a=lists&keywords={name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content,"html.parser")
    # find the first product item in the search results
    grid = soup.find('div', class_='search_list')
    # extract the link from the 'a' tag inside the product item
    product_link = grid.find('a')['href']
    final_url = "http://www.beyond-pharma.com" + product_link
    response2 = requests.get(final_url)
    soup2 = BeautifulSoup(response2.content,"html.parser")
    # find the section containing the Chinese name and CAS number
    finalgrid = soup2.find("div", class_="about_det pro_det")
    # extract the Chinese name and CAS number from the section
    print(finalgrid.text.strip())

print(BeyondPharma("udenafil"))
