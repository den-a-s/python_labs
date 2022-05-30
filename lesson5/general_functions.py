import io
from os import getcwd

def load_file(name: str, mode: str) -> io.TextIOWrapper | io.FileIO:
    file = open(name, mode, encoding='utf-8')
    return file