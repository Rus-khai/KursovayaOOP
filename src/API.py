import requests
from abc import ABC, abstractmethod


class ApiAbc(ABC):

    @abstractmethod
    def connect_api(self):
        pass

    @abstractmethod
    def load_vacancies(self):
        pass


class ApiHh(ApiAbc):
    """
    Класс для работы с API HeadHunter

    """
    def __init__(self, name):
        self.__name = name
        self.__url = 'https://api.hh.ru'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': self.__name , 'page': 0, 'per_page': 100}
        self.vacancies = []

    def connect_api(self):

        try:
            while self.params.get('page') != 20:
                response = requests.get(self.__url + '/vacancies', params=self.params)
                result = response.json()['items']
                self.vacancies.extend(result)
                self.params['page'] += 1
                result_vacancies = self.vacancies
            return result_vacancies
        except Exception as e:
            print(f'Ошибка при подключении: {e}')
            return 0
        else:
            return 0

    def load_vacancies(self):
        # self.params['text'] = text
        pass


if __name__ == "__main__":
    text_info = ApiHh('оператор').connect_api()
    print(text_info)
    connect_info = ApiHh.connect_api
    print(connect_info)
    # self.params['name'] = keyword
    # while self.params.get('page') != 20:
    #     response = requests.get(self.url + "/areas")
    #     vacancies = response.json()['items']
    #     self.vacancies.extend(vacancies)
    #     self.params['page'] += 1
