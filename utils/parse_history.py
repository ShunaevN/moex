import requests


def parse_history(url: str):
    print("Парсим данные")
    return requests.get(url).json()
