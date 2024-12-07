import requests

from src.parser import Parser


class HeadHunterAPI(Parser):

    def __init__(self):
        """Конструктор класса"""
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies = []
        super().__init__()

    def get_vacancies(self, keyword):
        """Функция, получающая данные по API"""
        try:
            self.__params["text"] = keyword
            while self.__params.get("page") != 20:
                response = requests.get(self.__url, headers=self.__headers, params=self.__params)
                if response.status_code == 200:
                    vacancies = response.json()["items"]
                    self.__vacancies.extend(vacancies)
                    self.__params["page"] += 1
                    return self.__vacancies
        except Exception as e:
            print(f"Ошибка получения данных {e}")
            return self.__vacancies
