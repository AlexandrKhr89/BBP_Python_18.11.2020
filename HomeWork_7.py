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
# и их координаты - кортежи (значения), созданные случайным образом с помощью модуля random в диапазоне от -10 до 10 по каждой оси.
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
persons = [{"name": "John", "age": 15}, {"name": "Jack", "age": 45}, {"name": "Jackson", "age": 5},
           {"name": "Bill", "age": 3}, {"name": "Gill", "age": 3}, {"name": "Gill_2", "age": 3}]

print(persons)
print(persons[0])
print(persons[0].keys())
print(persons[0].values())
print(persons[0].get("name"))
print(persons[0].get("age"))

min_age = 0
name_young = ''
most_long_name = ''
average_people_age = 0
name_young_name_list = []

for i, dict in enumerate(persons):
    # print(i, dict, dict.get("age"))
    if i == 0:
        min_age = dict.get("age")
        name_young = dict.get("name")
        # print(type(name_young))
        print('Самый молодой', name_young, ', ему', min_age, 'лет')
    elif dict.get("age") < min_age:
        min_age = dict.get("age")
        name_young = dict.get("name")
        print('Самый молодой', name_young, ', ему', min_age, 'лет')

    elif dict.get("age") == min_age:
        #     # name_young_name_list
        #
        print('Самым молодым', min_age, 'лет\nих имена:', name_young, dict.get("name"))

####################################################################################################
# 5) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]}
