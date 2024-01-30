# В некоторой школе решили набрать три новых математических класса 
# и оборудовать кабинеты для них новыми партами. 
# За каждой партой может сидеть два учащихся. 
# Известно количество учащихся в каждом из трех классов. 
# Выведите наименьшее число парт, которое нужно приобрести для них. 
# Input: 20 21 22(ввод чисел НЕ в одну строку) Output: 32

import math

per_day = int(input('Сколько машина проезжает за день: '))
total = int(input('Сколько машина должна проехать: '))

result = -(-total//per_day)
print(result)

result = math.ceil(total/per_day)
print(result)
result = total//per_day + (total%per_day != 0)
print(result)
result = (total + per_day - 1)//per_day
print(result)
