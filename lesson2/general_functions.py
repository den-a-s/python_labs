import numpy as np

def array_int() -> np.ndarray:
    tmp = input().split(" ")
    array = np.zeros(len(tmp), dtype=np.int64)
    for i in np.arange(len(tmp)):
        array[i] = tmp[i]
    return array