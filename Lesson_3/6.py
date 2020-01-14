'''
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
'''

import random

N = 10
LIST = [random.randint(1, 40) for i in range(N)]
print(LIST)

COUNT = LIST[0]

MIN_INDEX = LIST.index(min(LIST))
MAX_INDEX = LIST.index(max(LIST))

if MIN_INDEX > MAX_INDEX and MIN_INDEX - MAX_INDEX > 1:
    MIN_INDEX = LIST[MAX_INDEX + 1:MIN_INDEX]
    print('Список:', MIN_INDEX)
elif MIN_INDEX < MAX_INDEX and MAX_INDEX - MIN_INDEX > 1:
    MIN_INDEX = LIST[MIN_INDEX + 1:MAX_INDEX]
    print('Список:', MIN_INDEX)
else:
    print('Самое малое число и самое большое стоят подряд')
