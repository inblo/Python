text = input('Введите слово: ')
first = text[0]
length = len(text)
rest = text[1:length]
if first != 'a' or first != 'e' or first != 'i' or first != 'o' or first != 'u':
    newword = first + rest + 'ay'
else:
    newword = text + 'way'
print(newword.lower())
