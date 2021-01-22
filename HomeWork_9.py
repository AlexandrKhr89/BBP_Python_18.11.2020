import random
import string

########################################################################
# Цель задания - создать функции, которые будут генерировать случайные
# данные нужного формата # для записи в файлы разных типов.
#
# Функция 1. Создает данные для записи в файл txt.
# Функция генерирует и возвращает строку случайной длинны
# (не менее 100 но не более 1000 символов).
# В строке должны присутствовать большие и маленькие буквы английского
# алфавита, цифры, пробелы, знаки препинания, символ перехода на новую
# строку (\n).
# Строка должна выглядеть как текст.
# Слова отделяться друг от друга пробелами.
# Большие буквы только в начале слов.
# Цифры не должны быть частями слов, а стоять отдельно.
# Знаки препинания всегда идут в конце слова.
#
print("\nTask 1/4")


def my_word():
    my_word = random.choice(string.ascii_uppercase)
    for i in range(0, random.randint(2, 12)):
        my_word += random.choice(string.ascii_lowercase)
    return my_word


def my_number():
    my_number = str(random.choice(range(0, 9)))
    my_end_number_range = range(0, random.randint(0, 9))
    for i in my_end_number_range:
        my_number += str(random.choice(range(0, 9)))
    return my_number


def function_1():
    my_end_range = range(0, random.randint(100, 999))

    my_str = ' '

    for i in my_end_range:
        my_list = []
        my_punctuation_list = [',', '\n', '.', '!', '?', ';', ':', '', '', '', '']

        my_list.append(my_word() + random.choice(my_punctuation_list))
        my_list.append(my_number() + random.choice(my_punctuation_list))

        part_str = ' '.join(my_list[::])
        if (len(my_str) + len(part_str)) < 999:
            my_str += ' ' + part_str
        else:
            print('\nlength my_str = ', len(my_str))
            break

    return my_str


print('my_str :\n\n', function_1())

########################################################################
# Функция 2. Создает данные для записи в файл json.
# Создает и возвращает словарь со случайным количеством ключей
# (не менее 5 но не более 20 ключей).
# Ключи - уникальные случайные строки длинны 5 символов из маленьких
# букв английского алфавита (можно с повторениями символов).
# Значения - или целое число в диапазоне от -100 до 100,
# или число типа float в диапазоне от 0 до 1,
# или True/False. Выбор значения должен быть равновероятным.
# Т.е. вероятность того, что значение будет целым
# такая же, как и вероятность того, что будет типа float или типа bool.

print("\nTask 2/4")


def my_random_key():
    my_str = string.ascii_lowercase
    # print(my_str)
    key = ''
    for i in range(0, 5):
        # print(i)
        key += random.choice(my_str)
        # print(key)
    return key


print('my_random_key():', my_random_key())


def function_2():
    key_count = random.randint(5, 20)
    print('key_count =', key_count, type(key_count))
    my_int = random.randint(-100, 100)
    print('my_int =', my_int)
    my_float = random.random()
    print('my_float =', my_float)
    my_value_list = [True, False, my_float, my_int]
    my_dict = {}
    print('my_dict =', my_dict)
    print('my_random_key():', my_random_key())

    for i in range(0, key_count):
        # print(i)
        # print('my_random_key():', my_random_key())
        my_dict.update({my_random_key(): random.choice(my_value_list)})
        # print(i, 'my_dict =', my_dict)
    return my_dict


print('Данные для записи в файл json:\n', function_2())

########################################################################
# Функция 3. Создает данные для записи в файл csv.
# Создает и возвращает список длинны n внутренних списков длинны m
# (таблица с n строк и m столбцов).
# Числа n и m выбираются случайно в диапазоне от 3 до 10.
# В таблицу записывать значения только 0 или 1.
# Заголовка у таблицы нет.
########################################################################
# А теперь основное задание:
# Написать функцию generate_and_write_file которая принимает один
# параметр - полный путь к файлу.
# В зависимости от расширения файла (txt, csv, json) сгенерировать
# данные для записи и записать в данный файл.
# Если расширение не соответствует заданным,
# то вывести текст "Unsupported file format"
