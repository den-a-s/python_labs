from typing import Callable
from problems import problem1, problem2, problem3, problem4

def show_menu() -> None:
    menu = (
    "Выберите команду:",
    "1. Посчитать количество вхождений каждого слова в тексте. Отсортировать словарь по ключу.",
    "2. Посчитать количество вхождений каждой буквы в тексте. Отсортировать буквы по количеству вхождений.",
    "3. Для столицы из словаря, записанной в последней строке, определить страну.",
    "4. Для каждого города вывести название страны в отдельной строке в виде <город1> - <название страны>"
    )
    for elm in menu:
        print(elm)

def getting_task() -> Callable[[],None]:
    tasks = (problem1, problem2, problem3, problem4)
    cmd = int(input())
    if (cmd > 4 or cmd < 1):
        raise "Ошибка"
    return tasks[cmd - 1]