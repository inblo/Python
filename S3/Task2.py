# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) 
# на K элементов вправо,  K – положительное число. 
# Input:   [1, 2, 3, 4, 5] k = 3 Output:  [4, 5, 1, 2, 3]

l = [1, 2, 3, 4, 5] 
n = int(input('Введите показатель сдвига: '))

if n>=0:
    for i in range(n):
        ff = [0] * len(l)
        ff[0] = l[len(l)-1]
        for i in range(0, len(l)-1):
            ff[i+1] = l[i]
        l = ff
    print(ff)
else:
    for j in range(abs(n)):
        ff = [0] * len(l)
        ff[len(l)-1] = l[0]
        for i in range(len(l)-1, 0, -1):
            ff[i-1] = l[i]
        l = ff
    print(ff)