total = 0
for i in range(0, 5):
    num = int(input('Введите номер: '))
    ans = input('Вы хотите включить в сумму это число? (y/n) ')
    if ans == 'y':
        total = total + num
print(total)