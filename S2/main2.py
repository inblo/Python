# Дано натуральное число A > 1. Определите, 
# каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1. 
# Input:     5 Output:  6

# number = int(input('Введите натуральное число: '))
# fib = 1
# nofib = -1

# if number = fib

# while number > 1:
#     fact = fact * number
#     number = number - 1

# print(f'Число {number} не является числом Фибоначи! {nofib}')

# Вариант первый

A = int(input('Введите число '))
if A == 0:
    print(0)
elif A == 1:
    print(1)
else:
    F1 = 0
    F2 = 1
    n = 1
    Fn = 0
    while Fn < A:
        Fn = F1 + F2
        F1 = F2 
        F2 = Fn
        n += 1
    if Fn == A:
        print(n)
    else:
        print(-1)

# Вариант проще 
number = int(input('Введите число: '))

fibo_1, fibo_2 = 0, 1
count = 1
while fibo_2 < number:
    fibo_1, fibo_2 = fibo_2, fibo_1 + fibo_2
    count += 1

print(count if fibo_2 == number else '-1')