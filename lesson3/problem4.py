import numpy as np

def problem4() -> None:
    # Задание 4
    # На вход поступает число - количество строк.
    # Далее в каждой строке содержится название страны и некоторые города
    # (количество городов неизвестно) в следующем формате: <название страны> - <город1>, <город2>, <город3>, ... 
    # Для каждого города вывести название страны в отдельной строке в виде <город1> - <название страны>\
    cityDict = _get_input_dict()
    _output_dict(cityDict)

def _get_input_dict() -> dict:
    print("Введите количество строк: ")
    cnt = int(input())
    print("Введите ", cnt, "строк в виде: страна город1 город2 ... городN", cnt)
    cityDict = dict()
    for i in np.arange(cnt):
        list = input(str).split(" ")
        cityDict[list[0]] = list[1:]
    return cityDict

def _output_dict(dictionary:dict) -> None:
    for country in dictionary:
        for city in dictionary[country]:
            print(city, " - ", country)