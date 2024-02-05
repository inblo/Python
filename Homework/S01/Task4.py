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
