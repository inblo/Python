# Определите, можно ли от шоколадки размером 
# a × b долек отломить c долек, если разрешается 
# сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# Выведите yes или no соответственно.

# Решение автотеста
# if c <= b * a and (c % a == 0 or c % b == 0):
#     print('yes')
# else:
#     print('no')

n = int(input())
m = int(input())
k = int(input())
area = n * m
last = area - k
full_m = k / n
if full_m == (area - last):
     print('yes')
else:
    print('no')
