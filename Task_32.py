# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному 
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)


list1 = [1,3,5,3,4,9,11,44,28,13]
min_value = int(input("Input a min value: "))
max_value = int(input("Input a max value: "))
result = [i for i in range(len(list1)) if list1[i] > min_value and list1[i] < max_value]
print(result) 