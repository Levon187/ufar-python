import requests
from bs4 import BeautifulSoup

web_url='https://www.elitetraveler.com/finest-dining/restaurant-guide/the-13-best-restaurants-in-dubai'

def get_restaurants(web_url):

    req = requests.get(web_url)
    if req.status_code == 200:
        soup = BeautifulSoup(req.text, 'html.parser')  #html.parser #lxml
        restaurants=[]

        rest_elems = soup.find(class_='mon-font pb-1')

        restt1=rest_elems.find_all("strong")

        for i in range(0, len(restt1), 2):
            print(restt1[i].text)


get_restaurants(web_url)

