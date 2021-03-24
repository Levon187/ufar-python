import requests
from bs4 import BeautifulSoup


def get_cities_from_site(url):
    try:
        req = requests.get(url)
    except Exception as e:
        print(e)
        return

    if req.status_code == 200:
        soup = BeautifulSoup(req.text, 'html.parser')

        list_of_states_and_cities = soup.find('tr').text.strip().split("\n")

        while '' in list_of_states_and_cities:
            list_of_states_and_cities.remove('')

        for line in list_of_states_and_cities:
            state_city = line.split(" - ")
            get_city_temperature(state_city[1])


def get_city_temperature(city_name):
    city_name = city_name.lower()
    api_key = "7511ea4ed8c2d7e59d1ea3eb335be1b5"
    temp_type = "metric"
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units={temp_type}"

    response = requests.get(api_url)
    data = response.json()

    city_temperature = data["main"]["temp"]
    print(city_name.capitalize(), city_temperature)


site_url = "https://www.memory-improvement-tips.com/list-of-states-capitals.html"
get_cities_from_site(site_url)