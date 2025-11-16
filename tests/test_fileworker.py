from src.fileworker import FileWorker


def test_add_vacancy_and_delete_vacancy_FileWorker_try(vacancy_list_obj, capsys):
    json_saver = FileWorker()
    json_saver.add_vacancy(vacancy_list_obj[0])
    json_saver.add_vacancy(vacancy_list_obj[0])
    json_saver.delete_vacancies(vacancy_list_obj[0])
    captured = capsys.readouterr()
    assert captured.out.split('\n')[0] == 'Вакансия успешно добавлена'
    assert captured.out.split('\n')[1] == 'Данная вакансия уже есть в списке'
    assert captured.out.split('\n')[2] == 'Вакансия успешно удалена'


def test__and_delete_vacancy_JSONSaver_not_vacancy(vacancy_obj, capsys):
    json_saver = FileWorker()
    test_data = 'это не вакансия'
    json_saver.delete_vacancies(vacancy_obj)
    json_saver.delete_vacancies(test_data)
    captured = capsys.readouterr()
    assert captured.out.split('\n')[0] == 'Данной вакансии нет в списке'
    assert captured.out.split('\n')[1] == 'Объект не является экземпляром класса Vacancy и не может удален'


def test_filter_vacancies_JSONSaver_filter_words(vacancy_obj, capsys):
    json_saver = FileWorker()
    json_saver.add_vacancy(vacancy_obj)
    test_data = json_saver.get_vacancy(filter_words='опыт работы Python')
    print(test_data)
    captured = capsys.readouterr()
    assert captured.out.split('\n')[1] == "[{'name_vacancy': 'Python Developer', \
'url_vacancy': 'https://hh.ru/vacancy/123456>', \
'salary': '1000000 - 1500000 руб.', \
'requirements': 'Требования: опыт работы Python от 3 лет...'}]"
    json_saver.delete_vacancies(vacancy_obj)


def test_filter_vacancies_JSONSaver_filter_salary_top_n(vacancy_obj, capsys):
    json_saver = FileWorker()
    json_saver.add_vacancy(vacancy_obj)
    test_data = json_saver.get_vacancy(salary_range=1000000, top_n=10)
    print(test_data)
    captured = capsys.readouterr()
    assert captured.out.split('\n')[1] == "[{'name_vacancy': 'Старший Python разработчик', 'url_vacancy': 'https://hh.ru/vacancy/126807587', 'salary': '12000000 валюта не задана', 'requirements': 'КОММЕРЧЕСКИЙ ОПЫТ работы разработки на МИКРО СЕРВИСАХ не менее 5 лет обязательно; (кандидаты без опыта, писатели телеграмм ботов, монолитными проектами...'}, {'name_vacancy': 'DevOps / AI-инженер', 'url_vacancy': 'https://hh.ru/vacancy/127072458', 'salary': '1800000 валюта не задана', 'requirements': 'Опыт работы с GPU-платформами Vast.ai, RunPod, TensorDock. 4. Владение <highlighttext>Python</highlighttext> или Bash для автоматизации задач. 5. Опыт настройки SSH...'}, {'name_vacancy': 'Оператор видеонаблюдения (2 смена)', 'url_vacancy': 'https://hh.ru/vacancy/127164507', 'salary': '4000000 валюта не задана', 'requirements': 'Ответственность и внимательность. Умение работать в команде. Свободное владение русским языком. Знание ПК.'}, {'name_vacancy': 'Оператор call-центра', 'url_vacancy': 'https://hh.ru/vacancy/123205254', 'salary': '3500000 валюта не задана', 'requirements': 'С грамотной и поставленной русской речью. - Опыт работы не обязателен.'}, {'name_vacancy': 'Python Developer', 'url_vacancy': 'https://hh.ru/vacancy/123456>', 'salary': '1000000 - 1500000 руб.', 'requirements': 'Требования: опыт работы Python от 3 лет...'}]"
    json_saver.delete_vacancies(vacancy_obj)
