# Задание №2

######################################################################

# 1) У вас есть переменная value, тип - int.
# Написать тернарный оператор для переменной new_value по такому правилу:
# если value меньше 100, то new_value равно половине значения value,
# в противном случае - противоположне value число

value = 123
new_value = value / 2 if value < 100 else value * (-1)
print("1)", new_value)

######################################################################

# 2) У вас есть переменная value, тип - int.
# Написать тернарный оператор для переменной new_value по такому правилу:
# если value меньше 100, то new_value равно 1, в противном случае - 0

value = 123
new_value = 1 if value < 100 else 0
print("2)", new_value)

######################################################################

# 3) У вас есть переменная value, тип - int.
# Написать тернарный оператор для переменной new_value по такому правилу:
# если value меньше 100, то new_value равно True, в противном случае - False

value = 123
new_value = True if value < 100 else False
print("3)", new_value)

######################################################################

# 4) У вас есть переменная my_str, тип - str. Заменить в my_str все маленькие буквы на большие.

my_str = "Hello"
my_str = my_str.upper()
print("4)", my_str)

######################################################################

# 5) У вас есть переменная my_str, тип - str. Заменить в my_str все большие буквы на маленькие.

my_str = "Hello"
my_str = my_str.lower()
print("5)", my_str)

######################################################################

# 6) У вас есть переменная my_str, тип - str.
# Если ее длинна меньше 5, то допишите в конец строки себя же.
# Пример: было - "qwer", стало - "qwerqwer".
# Если длинна не меньше 5, то оставить строку как есть.

my_str = "Hello"
my_str = my_str * 2 if len(my_str) < 5 else my_str
print("6)", my_str)

######################################################################

# 7) У вас есть переменная my_str, тип - str.
# Если ее длинна меньше 5, то допишите в конец строки перевернутую себя же.
# Пример: было - "qwer", стало - "qwerrewq". Если длинна не меньше 5, то оставить строку как есть.

my_str = "Hello"
my_str = my_str + my_str[::-1] if len(my_str) < 5 else my_str
print("7)", my_str)

######################################################################

# 8) У вас есть переменная my_str, тип - str.
# Вывести на экран все символы из этой строки, которые являются буквой или цифрой.

my_str = "Hello"
my_str = my_str if my_str.isalnum() else "В строке не только буквы и цифры"
print("8)", my_str)

######################################################################

# 9) У вас есть переменная my_str, тип - str.
# Вывести на экран все символы из этой строки, которые не являются буквой или цифрой.

my_str = "Hello| :) |"

str_isalnum = ""
str_isnotalnum = ""

for index in range(len(my_str)):
    if my_str[index].isalnum() == False or not my_str[index] != ' ':
        str_isalnum = str_isalnum + my_str[index]
    else:
        str_isnotalnum = str_isnotalnum + my_str[index]

print("9)", str_isalnum)



######################################################################

# 10) У вас есть переменная my_str, тип - str.
# Вывести на экран все символы из этой строки, которые не являются буквой или цифрой и не пробел.

my_str = "Hello| :) |"

#Удаляем пробелы из строки
my_list = my_str.split()
my_str = ''.join(my_list)

str_isalnum = ""
str_isnotalnum = ""

for index in range(len(my_str)):
    if my_str[index].isalnum() == False or not my_str[index] != ' ':
        str_isalnum = str_isalnum + my_str[index]
    else:
        str_isnotalnum = str_isnotalnum + my_str[index]

print("10)", str_isalnum)

######################################################################

# ПРИМЕЧАНИЕ:
# Фраза "У вас есть переменная my_str" означает, что вы можете написать
# my_str = "Test string 123 QWE"или что-то подобное на свое усмотрение.
# Делать ввод с клавиатуры не обязательно.