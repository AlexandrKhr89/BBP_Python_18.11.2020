import csv

with open("test.csv", "r") as csv_file:
    data=[]
    reader = csv.DictReader(csv_file, delimiter = ";")
    for row in reader:
        data.append(row)
print(data)
data.append(('name', '10', 'e-mail:' '20@gmail.com', 'text:' '30'))

with open("test_new.csw", "w") as csv_file:
    fieldname = data[0], key ()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=";")
    writer.writeheader()
    writer.writerows(data)








# with open("test.csv", "r") as csv_file:
#     data=[]
#     reader = csv.DictReader(csv_file, delimiter = ";")
#     for row in reader:
#         data.append(row)
# print(data)




# with open("test.csv", "r") as csv_file: #test.csv - файл книга
#     data = []
#     reader = csv.reader(csv_file, delimiter = "_")       #csv.reader(csv_file) - файл читатель
#     for row in reader:
#         data.append(row)
#         # print(row)#1
#         # print(row[0])#2
# print(data)

# 1_2_3_4
# 5_6_7_8
# 9_10_11
# F_S_T
# header = data(pop)
# for row in data[:1]:
#     print('e-mail:', row[1])
#













# import json
#
# with open("test.json", "r", encoding="utf-8") as json_file:
#     data = json.load(json_file)
#     data_txt = json_file.read()
# print(type(data), data)
# # print(data[0])
#
#
# # print(type(data_txt), data_txt)
# json_data = json.loads(data_txt)
# print(json_data)
#
# data["last_name"] = "Connor"
#
# with open("test_new.json", "w") as json_file:
#     json.dump(data, json_file)