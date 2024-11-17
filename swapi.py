import requests
from pathlib import Path


class APIRequester:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

        if self.base_url.endswith('/'):
            self.base_url = self.base_url.rstrip('/')

    def get(self, url=''):
        if url.startswith('/'):
            url = url.lstrip('/')

        link = f'{self.base_url}/{url}'
        try:
            response = requests.get(link)
            response.raise_for_status()
            return response
        except requests.HTTPError:
            print('Ошибка на стороне клиента или сервера')
        except requests.RequestException:
            print('Возникла ошибка при выполнении запроса')


class SWRequester(APIRequester):
    def get_sw_categories(self) -> list:
        response = self.get().json()
        return response.keys()

    def get_sw_info(self, sw_type: str) -> str:
        response = self.get(f'{sw_type}/')
        return response.text


def save_sw_data():
    Path('data').mkdir(exist_ok=True)

    sw_request = SWRequester('https://swapi.dev/api')
    categories = sw_request.get_sw_categories()

    for category in categories:
        path = f'data/{category}.txt'
        with open(path, 'w') as f:
            category_data = sw_request.get_sw_info(category)
            f.write(category_data)


if __name__ == '__main__':
    save_sw_data()


# api = APIRequester(base_url='https://swapi.dev/api')
# response = api.get()
# #print(response.json())

# sw_req = SWRequester(base_url='https://swapi.dev/api')
# print(sw_req.get_sw_categories())
# # print(sw_req.get_sw_info('people'))
