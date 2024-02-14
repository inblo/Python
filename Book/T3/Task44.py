berthday = int(input('Скольких людей Вы хотите пригласить на День рождения: '))
if berthday < 10:
    for i in range(0, berthday):
        name = input("Введите имена гостей: ")
        print(name, 'has been invited!')
else:
    print('Too many people')