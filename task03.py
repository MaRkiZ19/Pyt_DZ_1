'''
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
 Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
 Вам требуется написать программу, которая проверяет счастливость билета.
*Пример:*
385916 -> yes
123456 -> no

Решение без циклов
'''

number = int(input('Введите шестизначное число: '))
a = number
b = a%10
a = a//10
b = b + a%10
a = a//10
b = b + a%10
a = a//10
c = a%10
a = a//10
c = c + a%10
a = a//10
c = c + a
if number<100000 or number>999999:
    print('Введен неверный номер')
elif b==c:
    print('Yes')
else:
    print('No')