# Задание 1
# На вход поступает строка, в которой содержится текст. 
# Посчитать количество вхождений каждого слова в этот текст. Отсортировать словарь по ключу.

from dataclasses import replace
from math import nan
import copy
import operator

def getCountWords(text):
    list = text.split(" ")
    dictionary = dict()
    for elm in list:
        if not elm in dictionary:
            dictionary[elm] = 1
        else:
            dictionary[elm] = dictionary[elm] + 1
    return dict(sorted(dictionary.items(),key = lambda x: x[0]))

# Задание 2
# На вход поступает строка, в которой содержится текст. 
# Посчитать количество вхождений каждой буквы в этот текст. 
# Отсортировать буквы по количеству вхождений.



# Задание 3
# На вход поступает количество строк.
# Далее вводится последовательность строк.
# Каждая строка содержит название страны и название столицы.
# Для столицы из словаря, записанной в последней строке, определить страну.

def getCountryByCapital(capitalDict, capital):
    for country in capitalDict:
        if capitalDict[country] == capital:
            return country
    return None

