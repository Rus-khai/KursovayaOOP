from src.vacancy import Vacancy
import pytest


# Определение фикстуры для мокирования объекта requests.get
@pytest.fixture
def mock_get(requests_mock):
    def register_get(url, status_code=200, json={}):
        requests_mock.get(url, status_code=status_code, json=json)

    return register_get


@pytest.fixture
def vacancies2():
    vacancies = {"Тест прошел успешно!": "ok"}
    return vacancies


@pytest.fixture
def vacancy_obj():
    vacancy = Vacancy("Python Developer", "https://hh.ru/vacancy/123456>",
                      "1000000 - 1500000 руб.", "Требования: опыт работы Python от 3 лет...")
    return vacancy


@pytest.fixture
def vacancy_list_obj():
    vacancy_1 = Vacancy("Python Developer", "https://hh.ru/vacancy/123456>",
                        "90 000-100 000 руб.", "Требования: опыт работы от 3 лет...")
    vacancy_2 = Vacancy("Python Developer", "https://hh.ru/vacancy/123456>",
                        "110 000-150 000 руб.", "Требования: опыт работы от 3 лет...")
    vacancy_list = [vacancy_1]
    return vacancy_list
