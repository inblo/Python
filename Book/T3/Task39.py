num = int(input('Введите число от 1 до 12: '))
for i in range(0, 13):
    answer = i * num
    print(i, 'X', num, '=', answer)