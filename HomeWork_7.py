import random  # For task 1

####################################################################################################
# 1) Создать список из 20 случайных целых чисел в диапазоне от 1 до 100.
# Задание можно выполнить и через обычный цикл и через генератор списков.
#
print("\nTask 1 \n1.1 Решение через цикл for")

numbers_list = []
for i in range(20):
    random_number = random.randint(1, 100)
    numbers_list.append(random_number)
print('1.1 numbers_list: ', numbers_list)

print("\nTask 1 \n1.2 Решение через генератор цикла")

numbers_list = [random.randint(1, 100) for number in range(20)]
print('1.2 numbers_list: ', numbers_list)

####################################################################################################
# 2) Создать словарь triangle в который записать точки A B C (ключи),
# и их координаты - кортежи (значения), созданные случайным образом с помощью модуля random в диапазоне от -10 до 10
# по каждой оси.
#

print("\nTask 2")

triangle = {'A': (random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10)),
            'B': (random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10)),
            'C': (random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10))}

print('triangle:', triangle)

# 3) Создать функцию my_print, которая принимает в виде параметра строку и печатает ее
# с тремя символами * вначале и в конце строки.
# Пример:
# my_str = 'I'm the string'
# Печатает ***I'm the string***
#

print("\nTask 3")


def my_print(str):
    str_ends = '***'
    new_str = str_ends + str + str_ends
    # return new_str
    print(new_str)


my_str = "I'm the string"
my_print(my_str)

####################################################################################################
# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# в) Посчитать среднее количество лет всех людей из списка.
#

print("\nTask 4")

persons = [{"name": "Johnson", "age": 15},
           {"name": "Jack", "age": 45},
           {"name": "Jackson", "age": 5},
           {"name": "Bill", "age": 3},
           {"name": "Gill", "age": 13},
           {"name": "Gilly", "age": 13}]

NAME = []
AGE = []
min_age_index_list = []
name_length = []
max_name_index = []

print('\nPersons:')
for i in persons:
    print('\t', i["name"], '\t', i["age"])
    NAME.append(i["name"])
    AGE.append(i["age"])

for i, age in enumerate(AGE):
    if age == min(AGE):
        min_age_index_list.append(i)

if len(min_age_index_list) == 1:
    print('\n4а) Самого молодого человека зовут {}, ему всего {} лет.'.format(NAME[min_age_index_list[0]],
                                                                              AGE[min_age_index_list[0]]))
elif len(min_age_index_list) > 1:
    print("\n4а) Самых молодых зовут:")
    for value in min_age_index_list:
        print('\t{}\t{} лет'.format(NAME[value], AGE[value]))

for i, name in enumerate(NAME):
    # print('i = {}, name = {}, длина имени = {}'.format(i, name, len(name)))
    name_length.append(len(name))

for i, max_name in enumerate(name_length):
    if max_name == max(name_length):
        max_name_index.append(i)

if len(max_name_index) == 1:
    print('\n4б) Самое длинное имя: {}'.format(NAME[max_name_index[0]]))

elif len(max_name_index) > 1:
    print('\n4б) Самые длинные имена:')
    for i, name in enumerate(max_name_index):
        print('{}'.format(NAME[max_name_index[i]]))

####################################################################################################
# 5) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]}

print("\nTask 5")

my_dict_1 = {'key0': 0, 'key1': 1, 'key2': 2, 'key3': 3}
my_dict_2 = {'key2': 2, 'key3': 3, 'key4': 4}

my_list_1 = list(my_dict_1.keys())
my_list_2 = list(my_dict_2.keys())

my_list = my_list_1 + my_list_2

print('Даны словари:')
print('my_dict_1 = {}'.format(my_dict_1))
print('my_dict_2 = {}'.format(my_dict_2))
print('\n5a) список из ключей, которые есть в обоих словарях: ', my_list)

diffrence_keys_1 = list(set(my_list_1) - set(my_list_2))

print('\n5б) список из ключей, которые есть в первом, но нет во втором словаре:', diffrence_keys_1)

my_new_dict = {}

for i in diffrence_keys_1:
    new_dict = {i: my_dict_1[i]}
    my_new_dict.update(new_dict)

print('\n5в) Новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре:',
      my_new_dict)
