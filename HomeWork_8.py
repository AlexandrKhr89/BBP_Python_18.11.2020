import random
import string

#  Импорт random и string для задачи 3

########################################################################
# 1. Считать данные из файла domains.txt
# Названия интернет доменов поместить в список (названия сохранить без
# точки).
#
print("\nTask 1/3")

file_data = open('domains.txt', 'r')
str_file_data = file_data.read()
my_domains_list = str_file_data.replace('.', '').split('\n')
print(my_domains_list)
file_data.close()

########################################################################
# 2. Считать данные из файла names.txt и поместить в список только
# фамилии из файла.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число
# (таблица взята с википедии).
# Фамилия находится всегда на одной и той же позиции в строке.
#
print("\nTask 2/3")

file_names_data = open('names.txt', 'r')

my_names_list = []

for my_line in file_names_data.readlines():
    my_line_from_name = my_line[my_line.find('\t') + 1::1]
    my_line_name = my_line_from_name[0:my_line_from_name.find('\t')]
    my_names_list.append(my_line_name)

print(my_names_list)

########################################################################
# 3. Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать из списков, полученных в задачах 1 и 2 и
# переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
# Буквы в строке МОГУТ повторяться (перемешивание алфавита не подойдет,
# так как буквы не смогут повторяться)
#
# Пример вызова функции:
# e_mail = create_email(domains, names)
# print(e_mail)
#
# >>>miller.249@sgdyyur.com

print("\nTask 3/3")


def my_random_name(my_list: list):
    my_random_name = my_list[random.randint(0, len(my_list) - 1)]
    ss_str = ''
    for symbol in my_random_name:
        if symbol.isalpha():
            ss_str = ss_str + symbol
        elif not symbol.isalpha():
            ss_str = ss_str + symbol.replace(symbol, '_')
    return my_random_name


def my_random_number(a: int, b: int):
    my_random_number_ = random.randint(a, b)
    return my_random_number_


def my_random_str():
    my_end_range = random.randint(5, 7)
    my_str = ''
    for i in range(0, my_end_range):
        my_str += random.choice(string.ascii_lowercase)
    return my_str


def my_random_domains(domains: list):
    my_random_dom = domains[random.randint(0, len(domains) - 1)]
    return my_random_dom


def create_email(domains: list, names: list):
    my_names = my_random_name(names)
    my_number = str(my_random_number(0, 999))
    str_a_z = my_random_str()
    my_domains = my_random_domains(domains)
    create_email = my_names + '.' + my_number + '@' + str_a_z + '.' + my_domains

    return create_email


e_mail = create_email(my_domains_list, my_names_list)

print('Result e_mail: ', e_mail)

########################################################################
print("\nThat is all")
