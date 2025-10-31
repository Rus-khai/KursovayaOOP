from src.utils import create_vacancy_list_file
from config import json_file, data_output

# def test_create_vacansy_list_file(vacancy_obj, capsys):
#
#     result_vacancy = create_vacancy_list_file(json_file, 'продаж', 200000, 1)
#     print(result_vacancy[0])
#     captured = capsys.readouterr()
#     assert captured.out == "{'job_title': 'Старший специалист отдела продаж', \
# 'link_to_vacancy': 'https://hh.ru/vacancy/118898540', 'salary': '200000 руб', \
# 'requirements': 'Опыт в продажах. Активная жизненная позиция. Желание зарабатывать \
# от 200 000 рублей в месяц. Готовность работать много и с удовольствием.'}\n"
#
#     with open(data_output, 'r', encoding='UTF-8') as f:
#         data_txt = f.read()
#     assert data_txt == 'Данная вакансия уже есть в списке\n'