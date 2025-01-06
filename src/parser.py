from abc import ABC, abstractmethod


class Parser(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancies(self, *args, **kwargs):
        pass
