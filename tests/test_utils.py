from config import json_file
from src.utils import create_vacancy_list_file


def test_create_vacansy_list_file(vacancy_obj, capsys):
    # Исходная подготовка данных
    result_vacancy = create_vacancy_list_file(json_file, 'продаж', 200000, 1)
    print(result_vacancy[0])  # Выведем первую вакансию в консоль
    captured = capsys.readouterr()

    # Удаляем перенос строки из вывода перед сравнением
    actual_output = captured.out.strip()

    # Ожидаемая строка без перевода строки
    expected_output = "{'name_vacancy': 'Оператор 1С на заявки', 'url_vacancy': 'https://hh.ru/vacancy/127142558', 'salary': '0', 'requirements': 'Уверенный пользователь ПК. Желание обучаться и развиваться в области продаж. Внимательность к деталям и аккуратность в работе с документами. '}"

    # Производим сравнение
    assert actual_output == expected_output
