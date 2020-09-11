import requests


class GetProxy:

    @staticmethod
    def gen_proxy():
        curl = requests.get(
            '').text
        if 'limit' in curl:
            return None
        return {"http": curl, "https": curl}
