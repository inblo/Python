import math
v = float(input('Введите высоту целиндра: '))
radius = float(input('Введите радиус целиндра: '))
s = math.pi * (radius**2)
print(round(s * v, 3))
