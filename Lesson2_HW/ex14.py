""" Задача 14: 
Требуется вывести все целые степени двойки (т.е. числа вида 2k),
не превосходящие числа N. """

numberN = int(input('Введите число N: '))
i = 0
while i < numberN:
    if (2 ** i > numberN):
        break
    else:
        print(2 ** i)
    i += 1
    
    
""" def checkNumber():
    n = int(input("Введите n "))
    i = 0
    temp = 0
    while temp <= n:
        temp = 2 ** i
        i += 1
    print(step(i - 1))

def step(n):
    m = [2 ** i for i in range(n)]
    return m

checkNumber() """