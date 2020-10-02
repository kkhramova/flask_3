import requests
import json


class Request:
    rates = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
    def get_resp(self):
        try:
            return print(requests.get(self.rates))
        except:
            raise Exception

    def content_type(content):
        try:
            return json.loads(content)
        except:
            raise Exception

