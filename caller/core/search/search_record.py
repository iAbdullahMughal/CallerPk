import json

from caller.core.search.services.contact_data import ContactData
from caller.core.search.services.sim_location import SimLocation
from caller.core.search.services.teleem_pk import TeleemPk


class SearchRecord:
    is_valid = False
    __MOBILE_NUMBER__ = None

    def __init__(self, mobile_number):
        self.__simplify_number__(mobile_number)

    def __simplify_number__(self, mobile_number):
        _mobile_number = None
        for _digit in mobile_number:
            try:
                int(_digit)
                if not _mobile_number:
                    _mobile_number = _digit
                else:
                    _mobile_number = _mobile_number + _digit
            except ValueError:
                pass
        try:
            self.__MOBILE_NUMBER__ = str(_mobile_number)[-10:]
            if len(self.__MOBILE_NUMBER__) == 10:
                self.is_valid = True
            else:
                self.is_valid = False
        except:
            self.is_valid = False

    def get_report(self):
        generated_data = {
            'pak_data': {},
            'sim_info': {},
            'cnic_info': {},
        }
        if not self.is_valid:
            return False, None

        pak_data_obj = ContactData(self.__MOBILE_NUMBER__)
        status_code, content = pak_data_obj.get_report()
        if status_code:
            generated_data['pak_data'] = content
            if content['cnic']:
                cnic = content['cnic']
                teleem_pk_obj = TeleemPk(cnic)
                generated_data['cnic_info'] = teleem_pk_obj.get_report()

        sim_location_obj = SimLocation(self.__MOBILE_NUMBER__)
        generated_data['sim_info'] = sim_location_obj.get_report()

        print(json.dumps(generated_data))
        return True, generated_data
