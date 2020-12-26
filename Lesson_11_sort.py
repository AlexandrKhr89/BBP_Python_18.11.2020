# Функция сортировки
# Регулярные выражения
import re

my_str = "-19a00 - 1966"
ages = re.findall(r'[0-9]{4}', my_str)
print(ages)


def key_sorted_by_age(obj_dict):
    ages = re.findall(r'[0-9]{2,4}', obj_dict)


# Шаблоны
# [0-9]
# [a-z]
# [A-Z]
# [A-Za-z0-9]
# [0-9]{2} 2 -  цифры
# [0-9]{2,4} -  от 2 до 4 цифр
# [0-9]+     -  Хотябы одна ццифра
# *

###################################################################

def key_sorted_by_age(obj_dict):  # функции наззіваем глаголами действия
    age = obj_dict["age"]
    return age


##################################################################

def key_sorted_by_name(obj_dict):  # функции наззіваем глаголами действия
    name = obj_dict["name"]
    return name


##################################################################
def key_sorted_by_len_name(obj_dict):  # функции наззіваем глаголами действия
    return len(obj_dict["name"])


##################################################################


test_list = ['asd', 'zxc', 'q', 'we', "1", 'AAAAA']
new_list = sorted(test_list)
new_list = sorted(test_list, key=len)

print(new_list, test_list)
# test_list.sort()
# print(test_list)

###########################################################
numb_list = [1, 23, -2, -10]
new_numb = sorted(numb_list, key=abs)
print(numb_list, new_numb)

###########################################################


dict_list = [
    {"name": "John", "age": 52},
    {"name": "Jackob", "age": 22},
    {"name": "Bob", "age": 42}
]

new_dict_list = sorted(dict_list, key=key_sorted_by_age)
print(new_dict_list)

new_dict_list = sorted(dict_list, key=key_sorted_by_name)
print(new_dict_list)

new_dict_list = sorted(dict_list, key=key_sorted_by_len_name)
print(new_dict_list)
