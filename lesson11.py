import requests
from bs4 import BeautifulSoup    # pip install BeautifulSoup

site_url = 'https://hy.wikipedia.org/wiki/%D4%B4%D5%A5%D5%B6%D5%AB%D5%BD_%D4%B2%D5%A5%D6%80%D5%A3%D5%AF%D5%A1%D5%B4%D5%BA'


def process_site(site_url):
    try:
        req = requests.get(site_url)
    except Exception as e:
        print(e)
        return
    if req.status_code == 200:
        soup = BeautifulSoup(req.text, 'html.parser')
        # print(soup.prettify())

        info_box = soup.find(class_='infobox vcard')
        tr_list = info_box.find_all('tr')

        for elem in tr_list:
            images = (elem.find(class_='image'))
            if images:
                print('https://hy.wikipedia.org' + images['href'])


def get_current_temp(city):
    key = ''
    units = 'metric'
    url2 = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units={units}'

    resp = requests.get(url2)
    if resp.status_code != 200:
        return False
    data = resp.json()
    print(data['main']['temp'])

get_current_temp("yereVan")

