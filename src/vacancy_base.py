from abc import ABC, abstractmethod


class VacancyBase(ABC):

    __slots__ = ("name", "url", "salary_from", "salary_to", "salary_currency")

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __le__(self, other):
        pass

    @classmethod
    @abstractmethod
    def cast_to_object_list(cls, vacancies):
        pass
