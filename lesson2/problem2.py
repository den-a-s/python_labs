import numpy as np
from general_functions import array_int

def problem2() -> None:
    print("Введите массив: ", end="")
    list = array_int()
    print("Числа повторяющиеся в массиве: ")
    list = _repeated_numbers(list)
    print(*list, sep=" ")

def _repeated_numbers(list: np.ndarray) -> np.ndarray:
    repeatedNumbers = []
    for i in np.arange(list.size):
        if np.sum(list==list[i]) > 1:
            repeatedNumbers.append(list[i])
    repeatedNumbers = np.array(repeatedNumbers)
    repeatedNumbers.sort()
    return np.unique(repeatedNumbers)