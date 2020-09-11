import requests
from bs4 import BeautifulSoup

from callerpk.settings import SERVER_THREE


class TeleemPk:
    __CNIC__ = None

    def __init__(self, cnic):
        self.__CNIC__ = cnic

    def __requests__(self):
        data = {
            'tehsil': None,
            'division': None,
            'province': None,
            'gander': None,
        }
        url = SERVER_THREE
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

        try:

            payload = {'cnic': self.__CNIC__, 'cap': 'j5b', 'n': '1'}
            response = requests.post(url=url, headers=headers, data=payload)
            soup = BeautifulSoup(response.content, 'html.parser')
            rows = soup.findAll("font", {"color": "blue"})
            img = soup.findAll("img")

            i = 0

            gander = str(img[0])
            if 'f.png' in gander.lower():
                data['gander'] = 'Female'
            elif 'm.png' in gander.lower():
                data['gander'] = 'Male'
            else:
                data['gander'] = 'Unknown'
            for row in rows:
                if i == 0:
                    pass
                elif i == 1:
                    data['tehsil'] = row.text
                elif i == 2:
                    data['division'] = row.text
                elif i == 3:
                    data['province'] = row.text
                i = i + 1
        except Exception as e:
            print(e)
        return data

    def get_report(self):
        return self.__requests__()
