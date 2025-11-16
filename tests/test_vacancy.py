from src.vacancy import Vacancy


def test_eq_Vacancy(vacancy_list_obj, capsys):
    if vacancy_list_obj[0].__eq__(vacancy_list_obj[0]):
        print('Метод сравнения работает иправно')
    captured = capsys.readouterr()
    assert captured.out == 'Метод сравнения работает иправно\n'


def test_valid_requirements_Vacancy():
    vacancy = Vacancy("Python Developer", "https://hh.ru/vacancy/123456>",
                      "1000000 - 1500000 руб.", 'ddddd')
    assert vacancy.requirements == 'ddddd'


def test_to_dict__Vacancy(vacancy_obj, capsys):
    print(vacancy_obj.to_dict())
    captured = capsys.readouterr()
    assert captured.out == "{'name_vacancy': 'Python Developer', \
'url_vacancy': 'https://hh.ru/vacancy/123456>', \
'salary': '1000000 - 1500000 руб.', \
'requirements': 'Требования: опыт работы Python от 3 лет...'}\n"
