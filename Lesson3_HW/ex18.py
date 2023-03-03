""" Задача 18: 
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5 """
    
import random

num = int(input("Введите число N - количество элементов в массиве: "))
num_array = []

for i in range(num):
    num_array.append(random.randint(1, num))

print(num_array)

x = int(input("Задайте число X, к значению которого будем подбирать ближайшее: "))

close_value = num_array[0]
for i in num_array:
    if abs(i - x) < abs(close_value - x):
        close_value = i

print(f"Ближайшее к числу {x} = {close_value}")
