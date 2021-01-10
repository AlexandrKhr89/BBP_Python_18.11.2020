##################################################################
# 1. Дано целое число (int). Определить сколько нулей в этом числе.
#
print("\nTask 1")
my_number = 100001000
# my_number = int(input("Введите целое число: "))
print("my_number = ", my_number)
my_str_number = str(my_number)
my_zero_count = my_str_number.count("0")
print("Число содержит нулей:", my_zero_count, "шт")
#
##################################################################
# 2. Дано целое число (int). Определить сколько нулей в конце этого числа.
#
print("\nTask 2")
# my_number = int(input("Введите целое число: "))
my_str_number = str(my_number)
print("my_number = ", my_number)
my_zero_str = ""
if my_str_number.endswith("0"):
    for index in my_str_number[::-1]:
        if index == "0":
            my_zero_str = my_zero_str + index
        else:
            break
    print("В конце числа", my_number, "содержиться нулей:", my_zero_str.count("0"), "шт.")
else:
    print("В конце числа", my_number, "не содержиться нулей")

##################################################################
# 3a. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.
#
print("\nTask 3a")

my_list_1 = [0, 1, 2, 3, 4, 5]
my_list_2 = [0, 15, 20, 35, 40, 55]
print("my_list_1 = ", my_list_1)
print("my_list_2 = ", my_list_2)
# print("Числа из my_list_1 на четных местах : ", my_list_1[::2])
# print("Числа из my_list_2 на НЕчетных местах : ", my_list_2[1::2])
my_result = []

for value in my_list_1[::2]:
    my_result.append(value)

for value in my_list_2[1::2]:
    my_result.append(value)

print("my_result =", my_result)

# 3b. Даны списки my_list_1 и my_list_2. Создать список my_result в который
# вначале поместить четные элементы (ИМЕННО ЭЛЕМЕНТЫ) из my_list_1 и потом нечетные элементы из my_list_2.
# my_list_1 = [1,2,3,4,5], my_list_2 = [10, 15, 20, 25] -> my_result [2, 4, 15, 25]
#
print("\nTask 3b")

my_list_1 = [6, 7, 8, 9, 10, 11]
my_list_2 = [10, 11, 12, 13, 14, 15]
print("my_list_1 = ", my_list_1)
print("my_list_2 = ", my_list_2)

my_result = []

for value in my_list_1[::]:
    if value % 2 == 0:
        my_result.append(value)

for value in my_list_2[::]:
    if not value % 2 == 0:
        my_result.append(value)

print("my_result =", my_result)

# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]
#
print("\nTask 4")
my_list = [1, 2, 3, 4]
print("my_list =", my_list)
new_list = []

for value in my_list[1::1]:
    new_list.append(value)
new_list.append(my_list[0])
print("new_list =", new_list)

# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)
#
print("\nTask 5")
my_list = [1, 2, 3, 4]
print("my_list =", my_list)
my_list.append(my_list.pop(0))
print("my_list =", my_list)

# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133.

print("\nTask 6")
my_str = "43 больше чем 34 но меньше чем 56"

# for index in my_str:
    # print(index)
    # if index.isdigit():
    #     my_number = index
    #     print(my_number)
#
my_list_from_str = list(my_str)
print(my_list_from_str)

for index in my_list_from_str:
    print(index)


# 7. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
#
# 8. Дана строка my_str в которой символы не повторяются и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить часть строки между этими символами.
# my_str = "My_long str", l_limit = "o", r_limit = "t" -> sub_str = "ng s"
#
# 9. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".
#
# 10. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.
