num1 = int(input('Введите первое число: '))
total = num1 
agein = "y"
while total == "y":
    num2 = int(input('Введите второе число: '))
    total = total + num2
    agein = input('Do you want to add another number? y/n')
print('The total is', total)