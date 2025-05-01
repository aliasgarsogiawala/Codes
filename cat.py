import requests
from bs4 import BeautifulSoup
import re
import openai
from flask import Flask, render_template, request

app = Flask(__name__)
openai.api_key = 'YOUR API KEY'

def chemicalbook(casnumber):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3 Edge/16.16299'
    }
    url = f"https://www.chemicalbook.com/Search_EN.aspx?keyword={casnumber}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    grid = soup.find("table", class_="mbox")
    if grid is None:
        return ""
    else:
        cat = grid.find("tr")
        if cat is None:
            return ""
        else:
            return "Chemical Book " + cat.text.strip() + "\n"

def trc(casnumber):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3 Edge/16.16299'
    }
    url = f"https://www.trc-canada.com/products-listing/?searchBox={casnumber}&type=searchResult"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    grid = soup.find("ul", class_="chemDetails")
    cat = grid.find("li")
    return "TRC Canada " + cat.text.strip().replace("Catalogue Number", "CAT No: ") + "\n"

def SynZeal(casnumber):
    url = f"https://www.synzeal.com/en/search?q={casnumber}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    grid = soup.find("div", class_="product_price_rating")
    cat = grid.find("div")
    return "Synzeal " + cat.getText(strip=True) + "\n"

def guidechem(casnumber):
    return "No CAT number found for GuideChem\n"

def ask_bot(question):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        max_tokens=20,  # Adjust the max_tokens as per your requirements
        n=1,
        stop=None,
        temperature=0.0
    )
    answer = response.choices[0].text.strip()
    return "Answer: " + answer + "\n"

@app.route('/')
def index():
    return render_template('cat.html', output="")


@app.route('/cas', methods=['POST'])
def cas():
    casnumber = request.form['casnumber']
    output = ""

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3 Edge/16.16299'
    }
    url = f"https://in.search.yahoo.com/search;_ylt=AwrKBxwlQYhkp.MputW6HAx.;_ylc=X1MDMjExNDcyMzAwMgRfcgMyBGZyAwRmcjIDcDpzLHY6c2ZwLG06c2ItdG9wBGdwcmlkA0xPQUF4TVc5VHdhWTVJVHpzMG44NUEEbl9yc2x0AzAEbl9zdWdnAzAEb3JpZ2luA2luLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzE0BHF1ZXJ5A2NhcyUyMDIyNjAxLTU5LTgEdF9zdG1wAzE2ODY2NTExODg-?p=cas+{casnumber}&fr=sfp&fr2=p%3As%2Cv%3Asfp%2Cm%3Asb-top&iscqry="
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    grid = soup.find("div", id="web")
    grid2 = grid.find_all("li")
    i = 0
    lst = []
    for link in grid2:
        if i == 10:
            break
        if link is None or link.find("a") is None:
            continue
        else:
            name = link.find("div", class_="d-ib p-abs t-0 l-0 fz-14 lh-20 fc-obsidian wr-bw ls-n pb-4")
            pre = link.find("div", class_="compTitle options-toggle")
            if pre is None:
                continue
            href = pre.find("a")["href"]
            if name is None:
                continue
            newname = name.find("span").text.strip()
            if newname[4:-4] in lst:
                continue
            if newname[4:-4] == "chemicalbook":
                output += chemicalbook(casnumber)
            elif newname[4:-4] == "trc-canada":
                output += trc(casnumber)
            elif newname[4:-4] == "synzeal":
                output += SynZeal(casnumber)
            elif newname[4:-4] == "guidechem":
                output += guidechem(casnumber)
            elif newname[4:-4] == "pharmaffiliates":
                match = re.search(r'RU=(.+?)/', href)
                if match:
                    extracted_string1 = match.group(0)
                final = extracted_string1.replace("RU=", "").replace("%2f", "/").replace("%3a", ":")
                response = requests.get(final)
                soup = BeautifulSoup(response.content, "html.parser").text
                question = "whats the cat number from the data" + soup
                output += ask_bot(question)
            else:
                match = re.search(r'RU=(.+?)/', href)
                if match:
                    extracted_string = match.group(0)
                    finallink = extracted_string.replace("RU=", "").replace("%2f", "/").replace("%3a", ":")
                    response1 = requests.get(finallink)
                    soup1 = BeautifulSoup(response1.content, "html.parser")
                    grid = soup1.find("body")
                    if grid is None:
                        continue
                    else:
                        question = "What is the CAT number specific to this soup: " + grid.text.strip()
                    output += ask_bot(question)
            lst.append(newname[4:-4])
            i += 1
    return render_template('cat.html', output=output)

if __name__ == '__main__':
    app.run()
