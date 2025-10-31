
from src.API import ApiHh

def test_send_request_success(mock_get):
    # Регистрация успешной реакции на GET-запрос
    mock_get('https://api.hh.ru/vacancies', status_code=200, json={
        'items': [
            {'id': '1', 'name': 'Developer'},
            {'id': '2', 'name': 'Designer'}
        ]
    })

    # Выполнение запроса
    hh_api = ApiHh(text='Python Developer')
    result = hh_api.send_request()

    # Проверка результатов
    assert len(result['items']) == 2
    assert result['items'][0]['name'] == 'Developer'