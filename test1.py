import requests

def get_cities(country):
    username = 'your_username'  # Replace with your GeoNames username
    base_url = 'http://api.geonames.org/searchJSON'

    params = {
        'q': f'country:{country}',
        'maxRows': 10,  # Maximum number of cities to retrieve
        'username': username
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        city_names = [city['name'] for city in data['geonames']]
        return city_names
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []

# Example usage
country_input = input('Enter a country name: ')
cities = get_cities(country_input)

if cities:
    print(f"Cities in {country_input}:")
    for city in cities:
        print(city)
else:
    print("No cities found for the given country.")
