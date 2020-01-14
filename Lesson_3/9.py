'''
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
'''


import random

LIST1 = []
for i in range(5):
    LIST2 = []
    for j in range(5):
        LIST2.append(random.randint(1, 20))
    LIST1.append(LIST2)

print(LIST1)

TEMP_LIST = []
for i in range(5):
    MIN_LIST = []
    for j in range(5):
        MIN_LIST.append(LIST1[j][i])
    TEMP_LIST.append(min(MIN_LIST))
print(
    'Максимальный элемент среди минимальных элементов каждого слобца:',
    max(TEMP_LIST))
