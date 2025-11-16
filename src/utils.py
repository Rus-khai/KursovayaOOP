import contextlib
from config import data_output
from src.fileworker import FileWorker
from src.vacancy import Vacancy


def create_vacancy_list_file(json_f, filter_words='', salary_range=0, top_n=0) -> list:
    """Функция принимает путь до json файла с данными полученные от api Hh, считывает данные из файла,
    формирует лист с объектами класса Vacancy, сортирует его и добавляет словарь
    по каждому такому объекту в файл vacancy.json.
    Возвращает список словарей с вакансиями отфильтрованными по критериям"""

    vacancy_list = Vacancy.cast_to_object_list(json_f)
    vacancy_list.sort(reverse=True)

    if filter_words == '' and salary_range == 0 and top_n == 0:
        return vacancy_list

    result_list = []
    vacancy_saver = FileWorker()
    for result_obj in vacancy_list:
        result_list.append(result_obj.to_dict())
        with open(data_output, 'w', encoding='UTF-8') as f:
            with contextlib.redirect_stdout(f):
                vacancy_saver.add_vacancy(result_obj)

    result_vacancy = vacancy_saver.get_vacancy(filter_words, salary_range, top_n)

    return result_vacancy


# if __name__ == '__main__':
#
#     test_list = create_vacancy_list_file(json_file, 'продаж', 100000, 6)
