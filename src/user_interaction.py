def filter_vacancies(vacancies_list, filter_words):
    """Функция для фильтрации списка вакансий по ключевым словам"""
    filtered_vacancies = []
    for vacancy in vacancies_list:
        for i in filter_words:
            name = vacancy.get("name", "")

            if i.lower() in name.lower():
                filtered_vacancies.append(vacancy)

    return filtered_vacancies


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    """Функция для сортировки вакансий по диапазону зарплат"""
    filtered_vacancies_salary = []
    filtered_salary_range = salary_range.split()
    min_salary = int(filtered_salary_range[0])
    max_salary = int(filtered_salary_range[-1])

    for vacancy in filtered_vacancies:
        salary_from = vacancy.get("salary_from")
        salary_to = vacancy.get("salary_to")

        if salary_from is not None and salary_to is not None:
            try:
                salary_from = int(salary_from)
                salary_to = int(salary_to)
            except ValueError:
                continue
            if salary_from >= min_salary and salary_to <= max_salary:
                filtered_vacancies_salary.append(vacancy)

    return filtered_vacancies_salary


def sort_vacancies(filtered_vacancies):
    """Функция сортировки вакансий по зарплате"""
    sorted_vacancies = sorted(filtered_vacancies, key=lambda x: x["salary"].get("from", 0))
    return sorted_vacancies


def get_top_vacancies(filtered_vacancies, top_n):
    """Функция для вывода топ-н вакансий"""
    filtered_vacancies = filtered_vacancies[0:top_n]
    return filtered_vacancies


def print_vacancies(vacancies):
    """Функция для вывода вакансий в консоль"""
    return print(vacancies)
