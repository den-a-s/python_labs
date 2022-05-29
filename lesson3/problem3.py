import numpy as np

def problem3() -> None:
    # Задание 3
    # На вход поступает количество строк.
    # Далее вводится последовательность строк.
    # Каждая строка содержит название страны и название столицы.
    # Для столицы из словаря, записанной в последней строке, определить страну.
    capDict = _get_dict_country_and_capital()
    cap = _get_capital()
    country = _get_country_by_capital(capDict, cap)
    print(country, " - ", cap) if country != None else print("Такой страны не найдено")

def _get_dict_country_and_capital() -> dict:
    print("Введите количество строк: ")
    cnt = int(input())
    print("Введите ", cnt, "строк в виде: страна столица")
    capDict = dict()
    for i in np.arange(cnt):
        list = input(str).split(" ")
        capDict[list[0]] = list[1]
    return capDict

def _get_capital() -> str:
    print("Введите столицу: ")
    return input(str)

def _get_country_by_capital(capitalDict: dict, capital: str) -> dict | None:
    for country in capitalDict:
        if capitalDict[country] == capital:
            return country
    return None

