""" Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8  """


numberA = int(input('Введите число A: '))
numberB = int(input('Введите число B: '))

def power(numberA, numberB):
    if (numberB == 1):
        return numberA
    else:
        return (numberA * power(numberA, numberB - 1))
    
print(f'A в степени B =>> {power(numberA, numberB)}') 
    