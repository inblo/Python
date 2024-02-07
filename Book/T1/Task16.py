rain = input('Идет ли на улице дождь?')
rain = str.lower(rain)
if rain == 'yes':
    today = input('Ветренно ли на улице?')
    today = str.lower(today)
    if today == 'yes':
        print('It is too windy for an umbrella')
    else:
        print('Take an umbrella!')
else:
    print('Enjoy you day')
