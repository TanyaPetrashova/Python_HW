"""""
Задача 6: Вы пользуетесь общественным транспортом? Вероятно,
вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, 
где сумма первых трех цифр равна сумме последних трех. Т.е. билет 
с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется 
написать программу, которая проверяет счастливость билета.

*Пример:*
385916 -> yes
123456 -> no
"""""

ticket = int(input('Введите шестизначный номер билета: '))

if (ticket > 999999) or (ticket < 100000):
    print ('Вы ввели не шестизначный номер. Повторите ввод: ')
else:
    abc = ticket // 1000 
    dEf = ticket % 1000
    sum_abc = abc // 100 + abc // 10 % 10 + abc % 10 
    sum_dEf = dEf // 100 + dEf // 10 % 10 + dEf % 10
    if sum_abc == sum_dEf:
        print("Ваш билет счастливый!")
    else:
        print("В следующий раз вам повезет")

