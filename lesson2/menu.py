import myLib
from typing import Callable
from problems import problem1, problem2, problem3, problem4

def show_menu() -> None:
    menu = (
    "Выберите команду:",
    "1. Постройить двумерный массив. Отсортировать столбцы по возрастанию сумм значений элементов",
    "2. По введённой строке с числами найти значения, которые повторяются более одного раза",
    "3. Найти пересечения двух массивов",
    "4. Из массива чисел определить наибольшее число, которое можно построить"
    )
    for elm in menu:
        print(elm)

def getting_task() -> Callable[[],None]:
    tasks = (problem1, problem2, problem3, problem4)
    cmd = int(input())
    if (cmd > 4 or cmd < 1):
        raise "Ошибка"
    return tasks[cmd - 1]