# Иван Васильевич пришел на рынок и решил купить два арбуза:
# один для себя, а другой для тещи. Понятно, что для себя нужно 
# выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: 
# арбузов слишком много и он не знает как же выбрать самый легкий 
# и самый тяжелый арбуз? Помогите ему! Пользователь вводит одно 
# число N – количество арбузов. Вторая строка содержит N чисел, 
# записанных на новой строчке каждое. Здесь каждое число – 
# это масса соответствующего арбуза 
# Input: 5 -> 5 1 6 5 9 Output: 1 9

import random # импортируем в программу функцию рандомных чисел

MIN_WEIGHT = 1000  # Константы
MAX_WEIGHT = 45000

count_watermelons = int(input('Введите количество арбузов: '))

min_weight = MAX_WEIGHT
max_weight = MIN_WEIGHT

for _ in range(count_watermelons):
    watermelon = random.randint(MIN_WEIGHT, MAX_WEIGHT)
    if min_weight > watermelon:
        min_weight = watermelon
    if max_weight < watermelon:
        max_weight = watermelon
    print(watermelon, end=' ')

print(f'\n\nСамый легкий арбуз {min_weight} гр.\nСамый тяжелый арбуз {max_weight} гр.')