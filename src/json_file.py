import json
import os

from src.file_base import FileBase
from src.vacancy import Vacancy


class JSONFile(FileBase):
    def __init__(self, file_name="data/vacancies.json"):
        """Конструктор класса"""
        self.__file_name = file_name

    def add_vacancy(self, vacancy: Vacancy):
        """Функция для добавления вакансий в файл json"""
        if not os.path.exists(self.__file_name):
            with open(self.__file_name, "w", encoding="utf-8") as f:
                json.dump([], f)

        with open(self.__file_name, "r+", encoding="utf-8") as f:
            try:
                file_vacancies = json.load(f)
            except json.JSONDecodeError:
                file_vacancies = []

            dict_vacancy = {
                "name": vacancy.name,
                "url": vacancy.url,
                "salary_from": vacancy.salary_from,
                "salary_to": vacancy.salary_to,
                "requirement": vacancy.requirement,
            }

            if dict_vacancy not in file_vacancies:
                file_vacancies.append(dict_vacancy)

        with open(self.__file_name, "w", encoding="utf-8") as f:
            json.dump(file_vacancies, f, ensure_ascii=False, indent=4)

    def delete_vacancy(self, vacancy: Vacancy):
        """Функция для удаления вакансий из файла json"""
        with open(self.__file_name, "r+", encoding="utf-8") as f:
            file_vacancies = json.load(f)

            dict_vacancy = {
                "name": vacancy.name,
                "url": vacancy.url,
                "salary_from": vacancy.salary_from,
                "salary_to": vacancy.salary_to,
                "requirement": vacancy.requirement,
            }

            if dict_vacancy in file_vacancies:
                file_vacancies.remove(dict_vacancy)

        with open(self.__file_name, "w", encoding="utf-8") as f:
            json.dump(file_vacancies, f, ensure_ascii=False, indent=4)
