# Дан список чисел. Определите, сколько в нем встречается различных чисел. 
# Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6

my_list = [1, 1, 2, 0, -1, 3, 4, 4, 7, 8, 7]
my_list = set(my_list)
print(len(my_list))