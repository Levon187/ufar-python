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
        a = soup.find(name='table', attrs={'id': 'rb', 'class': 'rb'})
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
        rate_by = 2
        for i in keys:
            while 0 <= k % 8 <= 7:
                temp2.append(temp[k])
                k += 1
                if k % 8 == 0:
                    break
            bank_dict[i] = temp2
            temp2 = []

        sorted_banks = []
        for k, v in bank_dict.items():
            if not sorted_banks:
                sorted_banks.append({k: v})
                continue
            for i in range(len(sorted_banks)):
                if v[rate_by] >= list(sorted_banks[i].items())[0][1][rate_by]:
                    sorted_banks.insert(i, {k: v})
                    break
            else:
                sorted_banks.append({k: v})
        print(sorted_banks, len(sorted_banks))

        new_list = []
        fieldnames = ["Բանկի անվանում", "Առք(USD)", "Վաճառք(USD)", "Առք(EUR)", "Վաճառք(EUR)", "Առք(RUR)", "Վաճառք(RUR)",
                      "Առք(GBP)", "Վաճառք(GBP)"]

        with open('buy_usd.csv', 'w', encoding='utf-8', newline='') as buy:
            writer = csv.writer(buy)
            writer.writerow(fieldnames)

            for bank in sorted_banks:
                bank_data = list(bank.items())
                new_list.append(bank_data[0][0])
                for i in bank_data[0][1]:
                    new_list.append(i)
                writer.writerow(new_list)
                new_list = []

        temp_dict = {}

        with open('buy_usd.csv', 'rt', encoding='utf-8') as f:
            data = csv.reader(f)
            data = list(data)
            headers = data[0]

            for i in range(len(headers)):
                temp_dict[headers[i]] = data[1][i]

        with open('buy_usd.json', 'w', encoding='utf-8') as out_file:
            # indent is an optional parameter that adds spaces for readability
            # sort_keys is an optional parameter to save json keys in alphabetical order
            json.dump(temp_dict, out_file, indent=4, ensure_ascii=False)


url = "http://rates.am/"

get_rates_am(url)
