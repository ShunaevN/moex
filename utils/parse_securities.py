import requests


def parse_securities(url: str):
    return requests.get(url).json()
