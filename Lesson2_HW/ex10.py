""" Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть """


import random
n = int(input('Сколько всего монеток на столе? '))
list_coins = []

for i in range(n):
    number = round(random.randint(0, 1))    # где 0 - решка, 1 - орел
    list_coins.append(number)
print(list_coins)

count_reshka = list_coins.count(int('0'))   # количество монет решкой вверх           
count_orel = list_coins.count(int('1'))     # количество монет орлом вверх

if count_reshka < count_orel:
    print (f'Переверните {count_reshka} решки')
elif count_orel == 0 or count_orel == n:
    print (f'Все монеты лежат одной стороной вверх')
else:
    print (f'Переверните {count_orel} орлов')

    
