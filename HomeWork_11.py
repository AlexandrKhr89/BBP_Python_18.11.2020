import json
import re

# Задания
# data.json - файл с данными о некоторых математиках прошлого.
########################################################################
# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.
print("\nTask 1/4")


def read_data_file(file_name: str):
    with open(file_name, "r", encoding='utf-8') as json_file:
        # print('1 read_data_file:', 'open {}'.format(file_name))
        # print(json_file.read())
        my_data_from_json_file = json.load(json_file)
        json_file.close()
        # print('read_data_file:', type(my_data_from_json_file))
        # print('1 read_data_file:', 'close {}'.format(file_name))
    return my_data_from_json_file


read_data_file('data.json')

########################################################################
# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.

print("\nTask 2/4")


def key_sorted_by_name(obj_dict):
    return obj_dict["name"]


def sort_by_family(file_name: str):
    # print('            2 sort_by_family:', 'type =', type(read_data_file(file_name)))
    # print('            2 sort_by_family:', 'len =', len(read_data_file(file_name)))
    new_dict_list = sorted(read_data_file('data.json'), key=key_sorted_by_name)
    # print('          2  new_dict_list:', new_dict_list)
    return new_dict_list



# sort_by_family()
print(sort_by_family('data.json'))

########################################################################
# 3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.
# 4. Написать функцию сортировки по количеству слов в поле "text"
