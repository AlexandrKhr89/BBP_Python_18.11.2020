# Щелчек Таноса
# 1 Создать папку ./alphabet/ или проверить, что папка существует.
# 2. В папку ./alphabet/ поместить файлы вида а.txt, b.txt, ..., z.txt в которых
# будет записана строка алфавита, но с заменой буквы зи названия файла на прописную


import os
from os.path import join as p_join
from os.path import isfile
from string import ascii_lowercase as alphabet


# 4
def tanos_click(dirname):
    # files= os.listdir(dirname)
    # files= sorted(os.listdir(dirname))
    # files= sorted([file for file in os.listdir(dirname) if os.path.isfile(os.path.join(dirname, file))])
    files = sorted([file for file in os.listdir(dirname) if isfile(p_join(dirname, file))])
    files = list(set(files))
    print(files)
    files = list(set(files))  # Особенность множеств SET
    for file in list(set(files))[:len(files)//2]:
        os.remove(p_join(dirname, file))
    print(files)


# 3
def create_txt_files(dirname):
    for symbol in alphabet:
        file_name = os.path.join(dirname, f"{symbol}.txt")
        new_alphabet = alphabet.replace(symbol, symbol.upper())  # 4 заменой буквы зи названия файла на прописную
        write_txt_file(file_name, new_alphabet)


# 2
def write_txt_file(filename, data):
    with open(filename, "w") as txt_file:
        # txt_file.write("\n".join(data))
        txt_file.write(data)


# 1
def create_dir(dir_name):
    # Легче извиниться чем спрашивать разрешения
    try:
        os.mkdir(dir_name)
    except FileExistsError:  # Замалчивать ошибки нехорошо
        pass


dir_name = 'alphabet'
# create_dir(dir_name)
# create_txt_files(dir_name)
tanos_click(dir_name)
