from unittest.mock import patch

import pytest

from src.hh_api import HeadHunterAPI


@pytest.fixture
def test_api():
    return [
        {'id': '112422077',
         'premium': False,
         'name': 'Python-разработчик',
         'department': None,
         'area':
             {'id': '1003', 'name': 'Гомель', 'url': 'https://api.hh.ru/areas/1003'},
         'salary': None, 'type': {'id': 'open', 'name': 'Открытая'},
         'address': None, 'response_url': None, 'sort_point_distance': None,
         'url': 'https://api.hh.ru/vacancies/112422077?host=hh.ru',
         'snippet':
             {'requirement': 'Опыт работы со схожим стеком от полугода(нам важно решение конкретных задач,а не стаж).',
              'responsibility': 'Реализация подключения Facebook с помощью API к нашему продукту.'},
         },
        {'id': '112690973',
         'premium': False,
         'name': 'Python-разработчик (Junior)',
         'department': None,
         'area':
             {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'},
         'salary':
             {'from': 100000, 'to': 120000, 'currency': 'RUR', 'gross': False},
         'address': None, 'response_url': None, 'sort_point_distance': None,
         'url': 'https://api.hh.ru/vacancies/112690973?host=hh.ru',
         'snippet':
             {'requirement': 'Уверенное владение <highlighttext>Python</highlighttext>. '
                             'Умение писать SQL запросы. Аналитический склад ума. '
                             'Навык работы с технической документацией и требованиями. Умение разбираться в...',
              'responsibility': 'Исправление существующих и возникающих багов. '
                                'Взаимодействие с командой по проекту. Работа с системой контроля версий Git. '
                                'Разработка и тестирование backend...'}}
    ]


@patch("requests.get")
def test_head_hunter_api_requests(test_api):

    hh_api = HeadHunterAPI()
    assert type(hh_api) is HeadHunterAPI
