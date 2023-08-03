# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: 
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


size_of_array = int (input("Input a size of array: "))
diff = int (input("Input a difference of elements: ")) 
first_el = int (input("Input a first element: "))

for i in range(size_of_array):
    print(first_el + i * diff, end=' ')

