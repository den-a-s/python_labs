from typing import Callable
from people import DataPeople
from general_functions import load_file

def show_menu() -> None:
    menu = (
        "Выберите команду:",
        "1. Добавление человека в список",
        "2. Вывод ФИ и возраста человека по индексу",
        "3. Вывод всех людей по заданному возрасту",
        "4. Распечатать людей",
        "5. Удалить человека по номеру"
    )
    for elm in menu:
        print(elm)

def _getting_task() -> int:
    print("Введите команду: ")
    cmd = int(input())
    if (cmd > 6 or cmd < 1):
        raise "Ошибка"
    return cmd

def complete_the_task(dataPeople: DataPeople):
    while(True):
        cmd = _getting_task()
        if cmd == 1:
            file = load_file("peoples.txt", "r+")
            dataPeople.input_people(file)
        elif cmd == 2:
            dataPeople.print_people_on_index()
        elif cmd == 3:
            dataPeople.print_people_on_age()            
        elif cmd == 4:
            dataPeople.print()
        elif cmd == 5:
            file = load_file("peoples.txt", "r+")
            dataPeople.delete_people(file)
        elif cmd == 6:
            print("Выход")
            return
            