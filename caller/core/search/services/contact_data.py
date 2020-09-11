import requests
from bs4 import BeautifulSoup

from caller.core.search.helper.get_proxy import GetProxy
from caller.models import PhoneNumbersModel
from callerpk.settings import SERVER_ONE


class ContactData:
    __MOBILE_NUMBER__ = None

    def __init__(self, mobile_number):
        self.__MOBILE_NUMBER__ = mobile_number

    def __request__(self, use_proxy=True):
        number_details = {
            'phone_number': None,
            'cnic': None,
            'date': None,
            'name': None,
            'address': None,
            'address1': None,
            'address2': None,
            'city': None,
            'other_phone': None,
            'first_name': None,
            'last_name': None,
        }
        try:
            if not len(self.__MOBILE_NUMBER__) == 10:
                return False, None

            payload = {'cnnum': self.__MOBILE_NUMBER__}
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36'
                              ' (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

            response = requests.post(SERVER_ONE, headers=headers,
                                     data=payload)

            soup = BeautifulSoup(response.content, 'html.parser')
            table = soup.find(lambda tag: tag.name == 'table')
            rows = table.findAll(lambda tag: tag.name == 'tr')
            if rows:
                for row in rows:
                    content_element = row.find_all('td')
                    is_key = True
                    key_elem = None
                    for key_element in content_element:
                        if is_key:

                            key_elem = key_element.text
                            is_key = False
                        else:
                            if 'otherphone' in key_elem and len(key_element.text) > 3:
                                number_details['other_phone'] = key_element.text
                                # number_details['other_phone'] = ''
                            elif 'cnic' in key_elem and len(key_element.text) > 3:
                                number_details['cnic'] = key_element.text
                                # number_details['cnic'] = ''
                            elif 'date' in key_elem and len(key_element.text) > 3:
                                # number_details['date'] = ''
                                number_details['date'] = key_element.text
                            elif 'name' in key_elem and len(key_element.text) > 2:
                                number_details['name'] = str(key_element.text).title()
                            elif 'address' in key_elem and len(key_element.text) > 3:
                                number_details['address'] = key_element.text.title()
                                # number_details['address'] = ''
                            elif 'address1' in key_elem and len(key_element.text) > 3:
                                number_details['address1'] = key_element.text.title()
                            elif 'address2' in key_elem and len(key_element.text) > 3:
                                number_details['address2'] = key_element.text.title()
                                # number_details['address2'] = ''
                            elif 'city' in key_elem and len(key_element.text) > 3:
                                number_details['city'] = key_element.text.title()
                            elif 'lastname' in key_elem and len(key_element.text) > 2:
                                number_details['last_name'] = key_element.text.title()
                            elif 'firstname' in key_elem and len(key_element.text) > 2:
                                number_details['first_name'] = key_element.text.title()

                try:
                    del number_details['number']
                except:
                    pass
                number_details['phone_number'] = '0092' + self.__MOBILE_NUMBER__

            return True, number_details
        except Exception as e:
            print(e, use_proxy)
            if use_proxy:
                return self.__request__(use_proxy=False)
            else:
                return False, None

    def get_report(self):
        try:
            PhoneNumbersModel.objects.create(
                phone_number=self.__MOBILE_NUMBER__
            )
        except:
            pass
        return self.__request__()
