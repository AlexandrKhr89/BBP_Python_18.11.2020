####################################################################################################
# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate.

print("\nTask 1")

my_list = ["123456", "7890-=", "qwert", "yuiop", "asdfg", "hjkl;'"]
my_new_list = []

for i, str in enumerate(my_list):
    if i % 2 == 0:
        my_new_list.append(str[::-1])
    else:
        my_new_list.append(str)

print("my_list =", my_list)
print("my_new_list =", my_new_list)

####################################################################################################
# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".

print("\nTask 2")

my_list = ["123456", "7890-=", "qwert", "yuiop", "asdfg", "hjkl;'"]
my_new_list = []

for str in my_list:
    if str[0] == "a":
        my_new_list.append(str)

print("my_list =", my_list)
print("my_new_list =", my_new_list)

####################################################################################################
# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.

print("\nTask 3")

# my_list = ["123456", "7890-=", "qwert", "yuiop", "_sdfg", "hjkl;'"]
my_list = ["123456 a", "7890-=", "qwert", "yuiop", "asdfg", "hjkl;A'"]
my_new_list = []

for str in my_list:
    if str[str.find("a")] == "a" or str[str.find("A")] == "A":
        my_new_list.append(str)

print("my_list =", my_list)
if my_new_list != []:
    print("my_new_list =", my_new_list)
else:
    print('Нет элементов с символом "а" ')

####################################################################################################
# 4. Дан список my_list в котором могум быть как строки (type str) так и целые числа (type int).
# Создать новый список в который поместить только строки из my_list.

print("\nTask 4")

# my_list =[]
my_list = [123456, 7890, "qwert", "yuiop", "_sdfg", "hjkl;'"]
my_new_list = []

for value in my_list:
    if type(value) == type(123):
        # print(value, type(value))
        pass
    elif type(value) == type('123'):
        # print(value, type(value))
        my_new_list.append(value)
    else:
        print("else")
        pass

print("my_list: ", my_list)
if my_new_list != []:
    print("my_new_list:", my_new_list)
else:
    print("Строковых значений в списке нет")

####################################################################################################
# 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке только один раз.

print("\nTask 5")

my_str = "qwerty 1234 asdf 1234 asdf"
my_list = []

for symbol in my_str:
    if my_str.count(symbol) == 1:
        # print(symbol)
        my_list.append(symbol)

print('my_str:', my_str)
print('Символи которые встречаются только один раз в строке:', my_list)

####################################################################################################
# 6. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

print("\nTask 6")

# my_str_1 = ""
# my_str_2 = ""

my_str_1 = "qwerty 1234 asdf 1234 asdf"
my_str_2 = "qwerty 7890 jkl; 7890 jkl; qwerty"
my_list = []

my_set_1 = set(my_str_1)
my_set_2 = set(my_str_2)

print("my_str_1:", my_str_1)
print("my_str_2:", my_str_2)

if len(my_set_1) > len(my_set_2):
    more_length_set = my_set_1
else:
    more_length_set = my_set_2

for value in more_length_set:
    if value in my_set_1 and my_set_2:
        my_list.append(value)

if my_list != []:
    print("Общие символы в строках:", my_list)
elif my_str_1 == "" and my_str_2 != "":
    print('Строка my_str_1 пуста')
elif my_str_1 != "" and my_str_2 == "":
    print('Строка my_str_2 пуста')
elif my_str_1 == "" and my_str_2 == "":
    print('Строки my_str_1 и my_str_2 пусты')

####################################################################################################
# 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.

print("\nTask 7")

# my_str_1 = ""
# my_str_2 = ""

my_str_1 = "qwerty 1234 asdf 1234 asdf zxcv"
my_str_2 = "qwerty 7890 jkl; 7890 jkl; zxccvv qwert"

my_list = []

big_str = ""
small_str = ""

my_set_1 = set(my_str_1)
my_set_2 = set(my_str_2)

if len(my_set_1) > len(my_set_2):
    more_length_set = my_set_1
    big_str += my_str_1
    small_str += my_str_2
else:
    more_length_set = my_set_2
    big_str += my_str_2
    small_str += my_str_1

for value in more_length_set:
    if big_str.count(value) == 1 and small_str.count(value) == 1:
        my_list.append(value)

print("my_str_1:", my_str_1)
print("my_str_2:", my_str_2)
if my_list != []:
    print("Общие символы, которые встречаются по одному разу в строках:", my_list)
elif my_str_1 == "" and my_str_2 != "":
    print('Строка my_str_1 пуста')
elif my_str_1 != "" and my_str_2 == "":
    print('Строка my_str_2 пуста')
elif my_str_1 == "" and my_str_2 == "":
    print('Строки my_str_1 и my_str_2 пусты')

####################################################################################################
# 8. Описать с помощью словаря следующую структуру для конкретного человека (можно придумать):
# Фамилия
# Имя
# Возраст
# Проживание
#     Страна
#     Город
#     Улица
# Работа
#     Наличие
#     Должность

print("\nTask 8")

adress_key_list = ['Страна', 'Город', 'Улица']
work_key_list = ['Наличие', 'Должность']

adress_list = ['Украина', 'Днепр', 'Павла Ниринберга 10']
work_list = ['Да', 'програмист']

DICT_ADRESS = dict(zip(adress_key_list, adress_list))
DICT_WORK = dict(zip(work_key_list, work_list))

my_key_list = ['Фамилия', 'Имя', 'Возраст', 'Проживание', 'Работа']
my_value_list = ['Иванов', 'Иван', '33', DICT_ADRESS, DICT_WORK]

DICT_STRUCTURE = dict(zip(my_key_list, my_value_list))

# print(DICT_STRUCTURE)

####################################################################################################
# 9. Описать с помощью словаря следующую структуру (рецепт ненастоящего торта,
# придумать и указать граммы для продуктов):
# Составляющие
#     Коржи
#         Мука
#         Молоко
#         Масло
#         Яйцо
#     Крем
#         Сахар
#         Масло
#         Ваниль
#         Сметана
#     Глазурь
#         Какао
#         Сахар
#         Масло

print("\nTask 9")

CAKE_RECIPE_DICT = {'Составляющие':
                        {'Коржи':
                             {'Мука': '1000 гр.', 'Молоко': '2000 гр.', 'Масло': '3000 гр.', 'Яйцо': '4000 гр.'},
                         'Крем':
                             {'Сахар': '1000 гр.', 'Масло': '2000 гр.', 'Ваниль': '3000 гр.', 'Сметана': '4000 гр.'},
                         'Глазурь':
                             {'Какао': '1000 гр.', 'Сахар': '2000 гр.', 'Масло': '3000 гр.'}}}

####################################################################################################
print("\nThat is all")


