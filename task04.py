'''
Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
*Пример:*
3 2 4 -> yes
3 2 1 -> no
'''

n = int(input('Введите количество долек по горизонтали: '))
m = int(input('Введите количество плиток по вертикали: '))
k = int(input('Введите необходимое Вам количество долек: '))
if k%n==0 or k%m==0:
    print('Yes')
else:
    print('No')
