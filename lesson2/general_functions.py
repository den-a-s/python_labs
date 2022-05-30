from typing import Generic
import numpy as np
from numpy.typing import NDArray

def array_int() -> NDArray[np.int64]:
    tmp = input().split(" ")
    array = np.zeros(len(tmp), dtype=np.int64)
    for i in np.arange(len(tmp)):
        array[i] = tmp[i]
    return array