from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class FileBase(ABC):

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy):
        pass
