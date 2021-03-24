import requests
from bs4 import BeautifulSoup

site_url = 'https://www.planetware.com/world/top-cities-in-the-world-to-visit-eng-1-39.htm'

def get_cities(site_url):

    req = requests.get(site_url)

    if req.status_code == 200:
        soup = BeautifulSoup(req.text, 'html.parser')
        cities = []
        info_box = soup.find_all(class_ = 'sitename')

        for elem in info_box:
            elem = str(elem).removesuffix("</h2>")
            cities.append(elem.split('.'))

        final_cities = []

        for i in cities:
            final_cities.append(i[1].strip())
        final_cities = final_cities[:-1]

        return final_cities

def popular_cities_temperature(listik):
    for i in listik:
        new_url = "http://api.openweathermap.org/data/2.5/weather?q="+i+"&appid=7511ea4ed8c2d7e59d1ea3eb335be1b5&units=metric"

        req = requests.get(new_url)

        data = req.json()

        city_tep = data['main']['temp']

        print(i+" "+str(city_tep))


print(get_cities(site_url))
popular_cities_temperature(get_cities(site_url))