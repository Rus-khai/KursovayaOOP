import json
from abc import ABC, abstractmethod
from typing import Any, Dict, List
import os
import requests
from config import DATA_DIR


class ApiAbc(ABC):
    """Базовый абстрактный класс для API."""

    @abstractmethod
    def send_request(self) -> Dict[str, Any]:
        """Отправляет запрос на получение данных."""
        pass

    @abstractmethod
    def search_vacancies(self) -> List[Dict[str, Any]]:
        """Ищет вакансии по указанному запросу."""
        pass


class ApiHh(ApiAbc):
    """
    Реализация API HeadHunter для поиска вакансий.
    """

    def __init__(self, text):
        self._text = text
        self._api_url = 'https://api.hh.ru/vacancies'
        self.params = {'text': self._text, 'page': 0, 'per_page': 100}
        self.vacancies = []  # Список вакансий

    def __send_request(self) -> Dict[str, Any]:
        """
        Выполняет запрос к API и возвращает результат.
        """
        response = requests.get(self._api_url, params=self.params)
        if response.status_code != 200:
            raise Exception(f'Ошибка при отправке запроса: {response.text}')
        return response.json()

    def send_request(self) -> Dict[str, Any]:
        return self.__send_request()

    def search_vacancies(self):
        """
        Поиск вакансий по странице за страницей.
        """
        json_file = os.path.join(DATA_DIR, 'vacancies.json')

        try:
            while True:
                data = self.send_request()
                self.vacancies.extend(data.get('items'))
                next_page = data.get('page') + 1
                total_pages = data.get('pages')
                if next_page >= total_pages or not data.get('items'):
                    break

                # Переходим на следующую страницу
                self.params['page'] = next_page
                result_data = data.get('items')
                with open(json_file, 'w+') as f:
                    json.dump(result_data, f, indent=4)
                return result_data
        except Exception as e:
            print(f"Возникла ошибка: {e}")
            return []

# if __name__ == "__main__":
#     hh_connector = ApiHh('Python')
#     results = hh_connector.search_vacancies()
#     print(results)
