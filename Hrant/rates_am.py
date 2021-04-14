from bs4 import BeautifulSoup
import requests
import csv
import json


def get_rates_am(url):
    try:
        req = requests.get(url)
    except Exception as e:
        print(e)
        return

    bank_dict = {}
    keys = []
    temp = []
    if req.status_code == 200:
        soup = BeautifulSoup(req.text, 'html.parser')

        i = 0
        for a in soup.find_all(name='table', attrs={'id': 'rb', 'class': 'rb'}):
            for b in a.find_all(name='tr'):
                for c in b.find_all(name='td'):
                    elem = c.text
                    # print(elem, f"{i} iteration")

                    if 17 <= i <= 225 and i % 13 == 4:
                        keys.append(elem[1:])

                    if (0 <= i % 13 <= 2 or 8 <= i % 13 <= 12) and 21 <= i <= 236:
                        temp.append(elem)
                        i += 1
                        continue

                    i += 1

        temp2 = []
        k = 0
        for i in keys:
            while 0 <= k % 8 <= 7:
                temp2.append(temp[k])
                k += 1
                if k % 8 == 0:
                    break
            bank_dict[i] = temp2
            temp2 = []

        # print(bank_dict)
        new_list = []
        fieldnames = ["Բանկի անվանում", "Առք(USD)", "Վաճառք(USD)", "Առք(EUR)", "Վաճառք(EUR)", "Առք(RUR)", "Վաճառք(RUR)",
                      "Առք(GBP)", "Վաճառք(GBP)"]

        with open('rates_am.csv', 'w', encoding='utf-8', newline='') as rates:
            # fieldnames = [key for key in new_dict.keys()]
            writer = csv.writer(rates)
            writer.writerow(fieldnames)

            for key, value in bank_dict.items():
                new_list.append(key)
                for i in value:
                    new_list.append(i)
                writer.writerow(new_list)
                new_list = []

        list_of_dicts = []
        temp_dict = {}
        with open('rates_am.csv', 'rt', encoding='utf-8')as f:
            data = csv.reader(f)
            data = list(data)
            headers = data[0]

            for row in data:
                if row != headers:
                    for i in range(len(headers)):
                        temp_dict[headers[i]] = row[i]

                    list_of_dicts.append(temp_dict)
                    temp_dict = {}

        # print(list_of_dicts)

        with open('rates_am.json', 'w', encoding='utf-8') as out_file:
            # indent is an optional parameter that adds spaces for readability
            # sort_keys is an optional parameter to save json keys in alphabetical order
            json.dump(list_of_dicts, out_file, indent=4)


url = "http://rates.am/"

get_rates_am(url)
