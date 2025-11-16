import json
from abc import ABC, abstractmethod

from config import FILE_NAME
from src.vacancy import Vacancy


class FileWorkerAbc(ABC):
    """
    Абстрактный класс для работы с файлами вакансий
    """

    @abstractmethod
    def add_vacancy(self):
        pass

    @abstractmethod
    def delete_vacancies(self):
        pass

    @abstractmethod
    def get_vacancy(self):
        pass


class FileWorker(FileWorkerAbc):
    """
    Класс для работы с файлом вакансий
    """

    def __init__(self, json_file=FILE_NAME):
        self.__name_file = json_file

    def get_vacancy(self, filter_words='', salary_range=0, top_n=0) -> list:
        """ Метод получения данных из файла по указанным критериям"""

        with open(self.__name_file, 'r+', encoding='UTF-8') as f:
            vacancys_list = json.load(f)

        filter_words = filter_words.lower()
        filter_words_vacancies_list = []

        for vacancys_dict in vacancys_list:
            if filter_words != '':
                if filter_words in vacancys_dict.get('requirements').lower():
                    filter_words_vacancies_list.append(vacancys_dict)
            else:
                break

        filter_salary_vacancies_list = []

        if len(filter_words_vacancies_list) == 0:
            for vacancys_dict in vacancys_list:
                if int(vacancys_dict.get('salary').split(' ')[0]) >= salary_range:
                    filter_salary_vacancies_list.append(vacancys_dict)
        else:
            for filter_vacancies_dict in filter_words_vacancies_list:
                if salary_range == 0:
                    break
                else:
                    if int(filter_vacancies_dict.get('salary').split(' ')[0]) >= salary_range:
                        filter_salary_vacancies_list.append(filter_vacancies_dict)

        result_vacancies_list = []

        if top_n > 0:
            if len(filter_salary_vacancies_list):
                for salary_vacancies_dict in filter_salary_vacancies_list:
                    if top_n > 0:
                        result_vacancies_list.append(salary_vacancies_dict)
                        top_n -= 1
                    else:
                        break

            else:
                for filter_words_vacancies_dict in filter_words_vacancies_list:
                    if top_n > 0:
                        result_vacancies_list.append(filter_words_vacancies_dict)
                        top_n -= 1
                    else:
                        break

        else:
            if len(filter_salary_vacancies_list) > 0:
                result_vacancies_list = filter_salary_vacancies_list
            else:
                return filter_words_vacancies_list

        return result_vacancies_list

    def add_vacancy(self, vacancy='') -> None:
        """
        Метод для добавления вакансий в файл
        """
        if isinstance(vacancy, Vacancy):
            vacancy = vacancy.to_dict()

            with open(self.__name_file, 'r+', encoding='UTF-8') as file:
                data_vacancy = file.read()

            if not data_vacancy:
                data_vacancy = []
                data_vacancy.append(vacancy)
                with open(self.__name_file, 'w+', encoding='UTF-8') as f:
                    json.dump(data_vacancy, f, indent=4)
                    print('Вакансия успешно добавлена')

            else:
                vacancys_list = json.loads(data_vacancy)

                append_flag = False
                for vacancy_dict in vacancys_list:

                    if vacancy_dict.__eq__(vacancy):
                        print('Данная вакансия уже есть в списке')
                        append_flag = True

                if not append_flag:
                    vacancys_list.append(vacancy)
                    with open(self.__name_file, 'w+', encoding='UTF-8') as f:
                        json.dump(vacancys_list, f, indent=4)
                    print('Вакансия успешно добавлена')

        else:
            print('Объект не является экземпляром класса Vacancy и не может быть добавлен')

    def delete_vacancies(self, vacancy='') -> None:
        """Метод для удаления информации о вакансиях"""

        if isinstance(vacancy, Vacancy):

            with open(self.__name_file, 'r+', encoding='UTF-8') as f:
                vacancys_list = json.load(f)

            checking_delete = 0
            for vacancy_dict in vacancys_list:

                if vacancy_dict == vacancy.to_dict():
                    vacancys_list.remove(vacancy.to_dict())

                    with open(self.__name_file, 'w+', encoding='UTF-8') as f:
                        f.truncate(0)
                        json.dump(vacancys_list, f, indent=4)
                        print('Вакансия успешно удалена')

            if checking_delete == 0:
                print('Данной вакансии нет в списке')

        else:
            print('Объект не является экземпляром класса Vacancy и не может удален')


# # Корректный пример тестирования
# if __name__ == '__main__':
#     # Создание экземпляра класса FileWorker
#     test_obj = FileWorker()
#
#     # Добавление тестовых вакансий
#     test_2 = Vacancy('111111gffgfgf', 'https://hh.ru/vacancy/127027244', '', 'fnggfgf')
#     test_3 = Vacancy('59995oololoo', 'https://.kn,g', '2000000', '2000000')
#     test_4 = Vacancy('шеф', 'https://aurhfj', '60000', 'gfgfdfd шеф')
#     test_5 = Vacancy('кок', 'https://d4d', '100000', 'аваавава кок')
#     test_6 = Vacancy('кок', 'https://24gs3d', '50000', 'аваавава кок')
#     test_7 = Vacancy('сторож', 'https://44g', '20000', 'сторож ппр')
#     test_8 = Vacancy('59995o', 'https://srhd6', '10000', 'ппвавпавав 59995o')
#     test_9 = Vacancy('кок', 'https://dgdgs', '50000', 'аваавава кок')
#
#     # Добавление вакансий
#     test_obj.add_vacancy(test_2)
#     test_obj.add_vacancy(test_3)
#     test_obj.add_vacancy(test_4)
#     test_obj.add_vacancy(test_5)
#     test_obj.add_vacancy(test_7)
#     test_obj.add_vacancy(test_8)
#     test_obj.add_vacancy(test_6)
#     test_obj.add_vacancy(test_9)
#     test_obj.add_vacancy(test_9)  # Повторная попытка добавить одинаковую вакансию
#
#     # Удаление вакансии
#     test_obj.delete_vacancies(test_2)
#
#     # Получение вакансий по фильтру
#     print(test_obj.get_vacancy('', 51000, 10))
#
#     # Проверка типа объекта
#     print(type(test_2))
#
#     print(test_obj.get_vacancy('', 51000, 10))
#     print(type(test_2))
