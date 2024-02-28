number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
res = number1 // number2
res2 = number1 % number2
if number1 % number2 == 0:
    print(f'Если разделить', number1, 'на', number2, 'получится', res)
else:
    print(f'Если разделить', number1, 'на', number2, 'получится', res, 'с остатком', res2)
    