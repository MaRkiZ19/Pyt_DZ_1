num = int(input('Введите трехзначное число: '))
if num>999 or num<100:
    print('Неверное число, необходимо трехзначное число') 
else:
    sum = num%10
    num = num//10
    sum = sum + num%10
    num = num//10
    sum = sum + num
    print(sum)
