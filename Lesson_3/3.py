'''
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''
import random

N = 5
INDEX_MIN = 0
INDEX_MAX = 0
LIST = [random.randint(1, 30) for i in range(N)]

print('Original list:', LIST)

TEMP_MIN = LIST[0]
TEMP_MAX = LIST[0]

# Алгоритм нахождения наименьшего элемента списка и его индэкса
for i in range(N):
    if LIST[i] < TEMP_MIN:
        TEMP_MIN = LIST[i]
        INDEX_MIN = i

# Алгоритм нахождения наибольшего элемента списка и его индэкса
for i in range(N):
    if LIST[i] > TEMP_MAX:
        TEMP_MAX = LIST[i]
        INDEX_MAX = i

LIST[INDEX_MIN], LIST[INDEX_MAX] = TEMP_MAX, TEMP_MIN
print('Modified list:', LIST)
