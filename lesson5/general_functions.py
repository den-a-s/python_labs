import io
from os import getcwd

def load_file() -> io.TextIOWrapper | io.FileIO:
    file = open('peoples.txt', 'r+', encoding='utf-8')
    return file