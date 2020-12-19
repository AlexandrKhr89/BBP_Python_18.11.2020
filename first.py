# print("Hello!")
# print("Hello 2!")
my_int=10
my_float=10.0
my_str="10"

print(my_int, type(my_int))
print(my_float, type(my_float))
print(my_str, type(my_str))

result=my_int+my_float
print(result)

#result=my_int+my_str
#print(result)

result=my_int+int(my_str)
print(result)

result=my_str+str(my_float)
print(result)

value=input("Введи целое число и нажми Enter:  ")
print(value, type(value))
print(value*10)
value=int(value)
print(value*10)
