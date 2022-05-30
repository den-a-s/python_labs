from random import randrange
import numpy as np
from numpy.typing import NDArray

def problem1() -> None:
    matrix = _create_matrix()
    _output_matrix(matrix)
    _sort_cols_by_sums_elems(matrix, _sumsColsInMatrix(matrix))
    print("Матрица после преобразования: ")
    _output_matrix(matrix)

def _create_matrix() -> np.matrix[np.float64]:
    print("Введите число строк и столбцов: ")
    row, cols = int(input()), int(input())
    print("Заполнить рандомно? [y/n]:")
    questionRandom = str(input())
    matrix = None
    if questionRandom == 'y':
        matrix = _randomMatrix(row, cols)
    elif questionRandom == 'n':
        matrix = _inputMatrix(row, cols)
    return matrix

def _output_matrix(matrix: np.matrix[np.float64]) -> None:
    print(matrix)

def _inputMatrix(row: int, cols: int) -> np.matrix[np.float64]:
    matrix = np.zeros(shape=(row,cols))
    for i in np.arange(row):
        for j in range(0, cols):
            matrix[i][j] = np.floating(input())
    return matrix

def _randomMatrix(row: int, cols: int) -> np.matrix[np.float64]:
    print("Введите диапозон рандома: ")
    a, b = int(input()), int(input())
    matrix = (b - a) * np.random.random((row,cols)) + a
    return matrix

def _sumsColsInMatrix(matrix: np.matrix[np.float64]):
    sums = matrix.sum(axis=0)
    return sums

def _swap_cols(matrix: np.matrix[np.float64], first: int, second: int):
    for i in np.arange(len(matrix.tolist())):
        matrix[i][first], matrix[i][second] = matrix[i][second], matrix[i][first]

def _sort_cols_by_sums_elems(matrix: np.matrix[np.float64], sumElems: np.ndarray[np.float64]):
    for i in np.arange(sumElems.size - 1):
        for j in np.arange(sumElems.size - i - 1):
            if sumElems[j] < sumElems[j + 1]:
                sumElems[j], sumElems[j + 1] = sumElems[j + 1], sumElems[j]
                _swap_cols(matrix, j, j + 1)