import os

import pytest

from src.json_file import JSONFile
from src.vacancy import Vacancy

base_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_path, "../data/test_vacancies.json")


@pytest.fixture
def test_add_vacancy():
    return Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000",
                   "150 000", "Требования: опыт работы от 3 лет...")


def test_add_vacancy_json_file(test_add_vacancy):

    json_saver = JSONFile(file_path)
    json_saver.add_vacancy(test_add_vacancy)

    test_read_file = (
        '[\n'
        '    {\n'
        '        "name": "Python Developer",\n'
        '        "url": "<https://hh.ru/vacancy/123456>",\n'
        '        "salary_from": "100 000",\n'
        '        "salary_to": "150 000",\n'
        '        "requirement": "Требования: опыт работы от 3 лет..."\n'
        '    }\n'
        ']'
    )

    with open(file_path, encoding="utf-8") as file:
        assert test_read_file == file.read()


def test_delete_vacancy_json_saver(test_add_vacancy):

    json_saver = JSONFile(file_path)
    json_saver.add_vacancy(test_add_vacancy)
    json_saver.delete_vacancy(test_add_vacancy)

    with open(file_path, encoding="utf-8") as file:
        expected = '[]'
        assert expected == file.read()
