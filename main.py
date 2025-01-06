from src.hh_api import HeadHunterAPI
from src.json_file import JSONFile
from src.user_interaction import filter_vacancies, get_top_vacancies, get_vacancies_by_salary, print_vacancies
from src.vacancy import Vacancy


def user_interaction():
    """Функция для взаимодействия с пользователем"""

    # Создание экземпляра класса для работы с API сайтов с вакансиями
    platforms = HeadHunterAPI()

    search_query = input("Введите поисковый запрос: ")

    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = platforms.get_vacancies(search_query)

    # Преобразование набора данных из JSON в список объектов
    vacancy_list = Vacancy.cast_to_object_list(hh_vacancies)

    vacancy_dict_list = [vacancy.to_dict() for vacancy in vacancy_list]

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000

    #  Функция фильтрации вакансий по ключевым словам
    filtered_vacancies = filter_vacancies(vacancy_dict_list, filter_words)

    #  Функция сортировки вакансий по зарплате
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    #  Функция сортировки вакансий (вывод топ № вакансий)
    top_vacancies = get_top_vacancies(ranged_vacancies, top_n)

    #  Функция вывода вакансий в консоль
    print_vacancies(top_vacancies)

    # Пример работы контструктора класса с вакансиями
    vacancy1 = Vacancy(
        "Python Developer",
        "<https://hh.ru/vacancy/123456>",
        "100 000",
        "150 000 руб.",
        "Требования: опыт работы от 3 лет...",
    )
    vacancy2 = Vacancy(
        "Python Developer",
        "<https://hh.ru/vacancy/123457>",
        "50 000",
        "125 000 руб.",
        "Требования: опыт работы от 3 лет...",
    )

    # Сохранение информации о вакансиях в файл
    json_saver = JSONFile("data/vacancies.json")
    json_saver.add_vacancy(vacancy1)
    json_saver.add_vacancy(vacancy2)
    json_saver.delete_vacancy(vacancy1)


if __name__ == "__main__":
    user_interaction()
