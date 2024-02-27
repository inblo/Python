# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо

# from random import randint

# n_set = set(randint(1, 20) 
# for i in range(int(input('Введите кол-во элементов первого множества: '))))
# print(n_set)
# m_set = set(randint(1, 20) 
# for i in range(int(input('Введите кол-во элементов второго множества: '))))
# print(m_set)
# s_set = sorted(n_set.intersection(m_set))
# print(*s_set)

# Вариант автотеста
var1 = '5 4'
var2 = '1 33 5 7 9'
var3 = '2 33 4 5'

var1 = set()
var2 = [int(x) for x in var2.split()]
var3 = [int(x) for x in var3.split()]
for i in var2:
    for j in var3:
        if i == j:
            var1.add(i)
var1.discard(' ')
new_list = list(var1)
new_list.sort()
for i in new_list:
    print(i, end = " ")
