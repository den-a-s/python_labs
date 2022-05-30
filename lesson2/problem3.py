import numpy as np
from general_functions import array_int
from numpy.typing import NDArray

def problem3() -> None:
    print("Введите массив 1: ", end="")
    list1 = array_int()
    print("Введите массив 2: ", end="")
    list2 = array_int()
    listIntersection = intersectionLists(list1, list2)
    print(*listIntersection, sep=" ")

def find(array: NDArray[np.int64], elm: np.int64) -> bool:
    for i in array:
        if elm == i:
            return True
    return False

def intersectionLists(array1: NDArray[np.int64], array2: NDArray[np.int64]) -> NDArray[np.int64]:
    intersection_list = []
    if len(array1) > len(array2):
        array1, array2 = array2, array1
    for elm in array1:
        if find(array2, elm):
            intersection_list.append(elm)
    return np.array(intersection_list)