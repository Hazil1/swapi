import requests
import os


class APIRequester:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get(self, url=''):
        try:
            response = requests.get(f'{self.base_url}{url}')
            response.raise_for_status()
            return response
        except requests.HTTPError:
            print('Статус коды от 400 до 599')
        except requests.RequestException:
            print('Возникла ошибка при выполнении запроса')


class SWRequester(APIRequester):
    def get_sw_categories(self) -> list:
        url = 'https://swapi.dev/api/'
        pass

    def get_sw_info(self, sw_type) -> str:
        url = f'https://swapi.dev/api/{sw_type}/'
        pass

    def save_sw_data(self):
        pass


api = APIRequester(base_url='https://swapi.dev/')
response = api.get('api')
print(response)