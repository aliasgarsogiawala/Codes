import requests

API_KEY = '2f772bf263a60b5e3f7b2e6c5ad97fe0'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

while True:
    city = input("Enter a city name : ")
    if city.lower()=="quit":
        ask=input("Are u sure u want to exit?\n")
        if ask.lower()=="no":
            continue
        elif ask.lower()=="yes":
            break
        else:
            print("Invalid Input!Im gonna continue the code")
            continue
        

    request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    response = requests.get(request_url, headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3 Edge/16.16299'
        })

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]["description"]
        print(f"The weather is {weather}")
        temperature = round(data["main"]["temp"] - 273.15, 2)
        print(f"The temperature is {temperature}'C")
    else:
        print(response.status_code)