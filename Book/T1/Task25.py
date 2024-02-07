name = input('Введите Ваше имя: ')
if len(name) < 5:
    surname = input('Введите Вашу фамилию: ')
    name = name + surname
    print(name.upper())
else:
    print(name.lower())
