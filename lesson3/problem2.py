from general_functions import output_dict

def problem2() -> None:
    #Задание 2
    # На вход поступает строка, в которой содержится текст. 
    # Посчитать количество вхождений каждой буквы в этот текст. 
    # Отсортировать буквы по количеству вхождений.
    print("Введите текст: ")
    dictionary = _get_count_letter(input())
    print("Количество вхождений букв в отсортированном по ключе порядке: ")
    output_dict(dictionary)

def _get_count_letter(text: str) -> dict:
    text = text.replace(" ", "")
    dictionary = _counting_letter(text)
    return _sorted_dict(dictionary)

def _counting_letter(text: str) -> dict:
    dictionary = dict()
    for elm in text:
        if not elm in dictionary:
            dictionary[elm] = 1
        else:
            dictionary[elm] = dictionary[elm] + 1
    return dictionary

def _sorted_dict(dictionary: dict) -> dict:
    return dict(sorted(dictionary.items(), key = lambda x: x[1]))