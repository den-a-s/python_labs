import numpy as np
from typing import TypedDict, Callable
import io
from os import getcwd
from general_functions import load_file

class People(TypedDict):
    surname: str
    name: str
    age: np.int8
    index: np.int64

class DataPeople():
    def __init__(self, peoples: list[People] | None = None):
        self.peoples = peoples
        if peoples == None:
            self.peoples = list()

    def load(self) -> None:
        file = load_file()
        if not self._load_from_file(file):
            raise "Жопа"

    def _load_from_file(self, file: io.TextIOWrapper | io.FileIO):
        try:
            text = file.readlines()
            if len(text) != 0:
                for line in text: 
                    line = line.replace('\n', '')
                    tmp = line.split(" ")
                    self.peoples.append (
                        People(**{ 
                            "surname": tmp[0],
                            "name": tmp[1],
                            "age": int(tmp[2]),
                            "index": int(tmp[3])
                        })
                    )
        except:
            return False
        return True

    def print_people_on_index(self):
        print("Введите номер человека: ", end='')
        index = int(input())
        people = DataPeople._find_peoples(self, index, 
        lambda people, index: people["index"] == index
        )
        if people == None:
            print("Такого номера в списке нет.")
            return
        print(people[0]["surname"], people[0]["name"] + ",", people[0]["age"])

    def print_people_on_age(self):
        print("Введите возраст человека: ", end='')
        age = int(input())
        peoples = DataPeople._find_peoples(self, age,
        lambda people, age: people["age"] == age
        )
        if peoples == None:
            print("Такого возраста в списке нет")
            return
        for people in peoples:
            print(people["surname"], people["name"] + ",", people["age"])

    def _find_peoples(self, index: int, predicat: Callable[[People, int], bool]) -> list[People] | None:
        peoples = list()
        for people in self.peoples:
            if predicat(people, index):
                peoples.append(people)
        return peoples if len(peoples) != 0 else None

    def print(self):
        for people in self.peoples:
            print(people["surname"], people["name"] + ",", people["age"])

    def input_people(self, file: io.TextIOWrapper | io.FileIO):
        print("Введите человека в формате: фамилия имя возраст", end='')
        people = input().split(" ")
        self.peoples.append (
            {
                "surname": people[0],
                "name": people[1],
                "age": int(people[2]),
                "index": int(self.peoples[-1]["index"] + 1)
            }
        )
        for people in self.peoples:
            file.write(people["surname"] + ' ' + people["name"] + " " + str(people["age"]) + " " + str(people["index"]) + '\n')

    def delete_people(self, file: io.TextIOWrapper | io.FileIO):
        print("Введите номер человека: ", end='')
        index = int(input())
        size = len(self.peoples)
        for people in self.peoples:
            if people["index"] == index:
                self.peoples.remove(people)
        if(len(self.peoples) == size):
            print("Такого номера в списке нет")
            return
        file = open('peoples.txt', 'w', encoding='utf-8')
        for people in self.peoples:
            file.write(people["surname"] + ' ' + people["name"] + " " + str(people["age"]) + " " + str(people["index"]) + '\n')
        file.close()
        file = open('peoples.txt', 'r+', encoding='utf-8')


