from typing import Callable
from general_functions import array_int
import numpy as np

def problem4() -> None:
    print("Введите массив: ", end="")
    list = array_int().tolist()
    list = _convert_to_str(list)
    print("Максимальное число: ", end="")
    print(_max_number_made_constructed_list(list))

def _is_greater(str1: str, str2: str) -> bool:
    minLength = min(len(str1),len(str2))
    for i in np.arange(minLength):
        if str1[i] > str2[i]:
            return True
        if str1[i] < str2[i]:
            return False
    if len(str1) == len(str2):
        return True
    str = str1 if minLength != len(str1) else str2
    if str[minLength - 1] < str[minLength]:
        return minLength != len(str1)
    else:
        return minLength == len(str1)

def _max_number_made_constructed_list(list: list[str]) -> str:
    sort(list, _is_greater)
    list.reverse()
    str = ""
    for elm in list:
        str += elm
    return str

def sort(list: list[str], f: Callable[[str,str], bool]):
    for i in np.arange(len(list) - 1):
        for j in np.arange(len(list) - i - 1):
            if f(list[j], list[j + 1]):
                list[j], list[j + 1] = list[j + 1], list[j]

def _convert_to_str(list: list) -> list[str]:
    result = []
    for elm in list:
        result.append(str(elm))
    return result