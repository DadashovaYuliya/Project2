import pytest

from src.vacancy import Vacancy


@pytest.fixture
def vacancy1():
    return Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>",
                   "100 000", "150 000", "Требования: опыт работы от 3 лет...")


@pytest.fixture
def vacancy2():
    return Vacancy("Python Developer", "<https://hh.ru/vacancy/123457>",
                   "50 000", "100 000", "Требования: опыт работы от 3 лет...")


@pytest.fixture
def vacancy3():
    return ("Python Developer")


def test_init_vacancy(vacancy1, vacancy2):
    assert vacancy1.name == "Python Developer"
    assert vacancy1.requirement == "Требования: опыт работы от 3 лет..."
    assert vacancy2.url == "<https://hh.ru/vacancy/123457>"
    assert vacancy2.salary_to == "100 000"
    assert vacancy1.salary_from == "100 000"


def test_to_dict(vacancy1):
    assert vacancy1.to_dict() == {'name': 'Python Developer',
                                  'url': '<https://hh.ru/vacancy/123456>',
                                  'salary_from': '100 000',
                                  'salary_to': '150 000',
                                  'requirement': 'Требования: опыт работы от 3 лет...'}
