print('1: Прямой отсчет!')
print('2: Обратный отсчет!')
qwe = int(input('В каком направлении вести отсчет?  '))
if qwe == 1:
    num = int(input('Введите число, до которого необходимо провести отсчет: '))
    for i in range(0, num):
        print(i)
elif qwe == 2:
    num = int(input('Введите число меньше 20: '))
    for i in range(20, (num + 1), -1):
        print(i)
else:
    print('I dont understand')
