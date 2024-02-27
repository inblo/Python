again = "y"
count = 0
while again == "y":
    name = input('Введите имя того, кого хотите пригласить: ')
    print(name, ', has been invited!')
    count = count + 1
    again = input('Вы хотите еще кого-нибудь пригласить? y/n')
print("Вы пригласили", count, "человек свой День рождения!")
