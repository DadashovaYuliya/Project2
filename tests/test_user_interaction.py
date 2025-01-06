import pytest

from src.user_interaction import filter_vacancies, get_vacancies_by_salary


@pytest.fixture
def vacancies_list():
    return [
        {"name": "Python Developer",
         "url": "<https://hh.ru/vacancy/123457>",
         "salary_from": "50000",
         "salary_to": "125000",
         "requirement": "Требования: опыт работы от 3 лет..."
         },
        {"name": "Java",
         "url": "<https://hh.ru/vacancy/123457>",
         "salary_from": "50000",
         "salary_to": "155000",
         "requirement": "Требования: опыт работы от 3 лет..."
         },
        {"name": "Python",
         "url": "<https://hh.ru/vacancy/123457>",
         "salary_from": "50000",
         "salary_to": "135000",
         "requirement": "Требования: опыт работы от 3 лет..."
         },
        {"name": "Django",
         "url": "<https://hh.ru/vacancy/123457>",
         "salary_from": "100000",
         "salary_to": "125000",
         "requirement": "Требования: опыт работы от 3 лет..."
         }
            ]


def test_filter_vacancies_no_matches(vacancies_list):

    filter_words = ["java"]
    result = filter_vacancies(vacancies_list, filter_words)
    assert result == [{
            "name": "Java",
            "url": "<https://hh.ru/vacancy/123457>",
            "salary_from": "50000",
            "salary_to": "155000",
            "requirement": "Требования: опыт работы от 3 лет..."
        }]


def test_get_vacancies_by_salary(vacancies_list):

    salary_range = "80000 - 150000"
    expected_result = [
        {
            "name": "Django",
            "url": "<https://hh.ru/vacancy/123457>",
            "salary_from": "100000",
            "salary_to": "125000",
            "requirement": "Требования: опыт работы от 3 лет..."
        },
    ]
    result = get_vacancies_by_salary(vacancies_list, salary_range)
    assert result == expected_result
