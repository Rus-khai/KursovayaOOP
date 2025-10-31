import json
import re
from config import json_file, DATA_DIR
import os
class Vacancy:

    __slots__ = ('name_vacancy', 'url_vacancy', 'salary', 'requirements')
    name_vacancy: str
    url_vacancy: str
    salary: str
    requirements: str

    def __init__(self, name_vacancy, url_vacancy, salary, requirements):
        self.name_vacancy = name_vacancy
        self.url_vacancy = url_vacancy
        self.salary = salary
        self.requirements = requirements
        self.__validate()

    def __validate(self):
        """Приватный метод для валидации данных."""
        # Регулярное выражение для проверки URL
        valid_url_pattern = r'^https?:\/\/'

        # Проверка типа имени вакансии
        if not isinstance(self.name_vacancy, str):
            raise ValueError('Имя вакансии должно быть строкой.')

        # Проверка URL
        if not isinstance(self.url_vacancy, str) or not re.match(valid_url_pattern, self.url_vacancy):
            raise ValueError('URL вакансии должен быть строкой и начинаться с http(s).')

        # Проверка зарплаты
        if not isinstance(self.salary, str):
            raise ValueError('Заработная плата должна быть строкой.')

        # Проверка требований
        if not isinstance(self.requirements, str):
            raise ValueError('Требования должны быть строкой.')

        return f"Вакансия '{self.name_vacancy}' успешно прошла валидацию."

    def __str__(self):
        if not self.salary == 0:
            self.salary == 'Зарплата не указана'

        result_str = f"'Название': {self.name_vacancy},\
         \n'Ссылка на вакансию': {self.url_vacancy},\
         \n'Зарплата': {self.salary},\
         \n'Описание': {self.requirements}\
         "
        return result_str
    # Сравнение вакансии по зарплате

    def __lt__(self, other):

        vacancy_salary = int(self.salary.split(" ")[0])
        other_salary = int(other.salary.split(" ")[0])
        return vacancy_salary < other_salary
    # Сравнение вакансии

    def __eq__(self, other):
        return self.url_vacancy == other.url_vacancy

    def to_dict(self):
        """Метод для представления данных о вакансии в словаре"""

        result_dict = {
            'name_vacancy': self.name_vacancy,
            'url_vacancy': self.url_vacancy,
            'salary': self.salary,
            'requirements': self.requirements
        }
        return result_dict

    @classmethod
    def cast_to_object_list(cls, json_file: str) -> list:
        """Метод принимает json файл с данными по вакансиям полученных по api
        и возвращает лист с объектами класса"""

        vacancies_list = []
        try:
            with open(json_file, 'r+') as f:
                vacancies_data = json.load(f)

        except FileNotFoundError as e:
            print(f'Файл не прочитан. Ошибка: {e}')

        else:
            for vacancy_dict in vacancies_data:
                name_vacancy = vacancy_dict.get('name')
                url_vacancy = vacancy_dict.get('alternate_url')

                if vacancy_dict.get('salary') is None:  # Валидация данных в ключе 'salary'
                    salary_from = None
                    salary_currency = ''
                else:
                    salary_from = vacancy_dict.get('salary').get('from')
                    salary_currency = vacancy_dict.get('salary').get('currency')

                requirements = vacancy_dict.get('snippet').get("requirement")

                if salary_currency == 'RUR':
                    salary_currency = 'руб'
                elif salary_currency == 'USD':
                    salary_currency = 'usd'
                elif salary_currency == 'EUR':
                    salary_currency = 'eur'
                else:
                    salary_currency = 'валюта не задана'

                if salary_from is not None:
                    salary = f'{salary_from} {salary_currency}'
                else:
                    salary = "0"

                vacancies_obj = cls(name_vacancy, url_vacancy, salary, requirements)
                vacancies_list.append(vacancies_obj)

        finally:
            return vacancies_list

# if __name__ == '__main__':
#
#     file = os.path.join(DATA_DIR, 'vacancies.json')
#     test = Vacancy.cast_to_object_list(file)
#     print(test)

    # test_1 = Vacancy.cast_to_object_list(file)

    # for obj in test_1:
        # print(obj)
        # print(obj.to_dict())
        # print(obj.name_vacancy)
        # print(obj.url_vacancy)
        # print(obj.salary)
        # print(obj.requirements)
        # print('-------------------------')
