import requests
from bs4 import BeautifulSoup
 
import re

url = "https://r.search.yahoo.com/_ylt=Awrx.w1lU4xko1kRCXW7HAx.;_ylu=Y29sbwNzZzMEcG9zAzYEdnRpZAMEc2VjA3Ny/RV=2/RE=1686946790/RO=10/RU=https%3a%2f%2fwww.pharmaffiliates.com%2fen%2f70020-54-1-8-methoxy-loxapine-pa120961001.html/RK=2/RS=B.3JkITE0XpTtvzBqroBMaadstI-"

match = re.search(r'RU=(.+?)/', url)
if match:
    extracted_string = match.group(1).replace("%2f","/").replace("%3a",":")
    # print(extracted_string)

response=requests.get(extracted_string)
soup=BeautifulSoup(response.content,"html.parser")
print(soup.text)
