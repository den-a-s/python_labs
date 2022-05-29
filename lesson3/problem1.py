from general_functions import output_dict

def problem1() -> None:
    # Задание 1
    # На вход поступает строка, в которой содержится текст. 
    # Посчитать количество вхождений каждого слова в этот текст. Отсортировать словарь по ключу.    
    text = _get_input_text()
    count_words = _get_count_words(text)
    print("Количество вхождений слов в отсортированном по ключе порядке: ")
    output_dict(count_words)

def _get_input_text() -> list[str]:
    print("Введите текст: ")
    text = str(input()).split(" ")
    return text

def _get_count_words(text: list[str]) -> dict:
    dictionary = _counting_word(text)
    return _sorted_dict(dictionary)    

def _counting_word(text:list[str]) -> dict:
    dictionary = dict()
    for elm in text:
        if not elm in dictionary:
            dictionary[elm] = 1
        else:
            dictionary[elm] = dictionary[elm] + 1
    return dictionary

def _sorted_dict(dictionary: dict) -> dict:
    return dict(sorted(dictionary.items(), key = lambda x: x[0]))