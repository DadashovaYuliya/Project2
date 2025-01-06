from src.vacancy_base import VacancyBase


class Vacancy(VacancyBase):
    __slots__ = ("name", "url", "salary_from", "salary_to", "requirement")

    def __init__(self, name, url, salary_from, salary_to, requirement):
        """Конструктор класса"""
        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.requirement = requirement

    @classmethod
    def __verify_data(cls, other):
        """Функция, проверяющая что другой объект относится к классу Vacancy или int"""
        if not isinstance(other, (int, Vacancy)):
            raise TypeError("Некорректное сравнение")

        return other if isinstance(other, Vacancy) else other.salary_from

    def __eq__(self, other):
        """Магический метод сравнения на равенство"""
        other_pay = self.__verify_data(other)
        return self.salary_from == other_pay

    def __le__(self, other):
        """Магический метод сравнения на меньше или равно"""
        other_pay = self.__verify_data(other)
        return self.salary_from <= other_pay

    @staticmethod
    def valid(data):
        """Проверка на валидность информации"""
        if isinstance(data, (float, int)) and data:
            return data
        else:
            return 0

    @classmethod
    def cast_to_object_list(cls, vacancies):
        """Функция, преобразующая данные, полученные с API в список объектов"""
        result = []
        for vacancy in vacancies:

            name = vacancy.get("name")
            url = vacancy.get("url")
            requirement = vacancy.get("requirement")

            if vacancy.get("salary"):
                salary_from = cls.valid(vacancy.get("salary", {"from": 0}).get("from"))
                salary_to = cls.valid(vacancy.get("salary", {"to": 0}).get("to"))

            else:
                salary_from = cls.valid(vacancy.get("salary_from", 0))
                salary_to = cls.valid(vacancy.get("salary_to", 0))

            vacancy_obj = cls(name, url, salary_from, salary_to, requirement)
            result.append(vacancy_obj)
        return result

    def to_dict(self):
        return {
            "name": self.name,
            "url": self.url,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "requirement": self.requirement,
        }
