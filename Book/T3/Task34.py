print('1) Square')
print('2) Tringle')
number = int(input('Enter a number: '))
if number == 1:
    k = int(input('Введите длинну стороны квадрата: '))
    print(f'Площадь квадрата равна', k * k)
elif number == 2:
    a = int(input('Введите длинну стороны треугольника: '))
    b = int(input('Введите высоту треугольника: '))
    print(f'Площадь треугольника равна', a * b // 2)
else:
    print('Введена некорректная цифра')
