'''
В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.

'''


import random

N = 10
LIST = [random.randint(1, 30) for i in range(N)]
print(LIST)

# Применяю мин и макс так как ранее реализовавыл свои алгоритмы
# Расписывать повторно не буду.
Z_MAX = max(LIST)
X_MAX = max(LIST)

for i in LIST:
    if i < Z_MAX:
        Z_MAX = i

if LIST.count(Z_MAX) > 1:
    print('Два минимальных числа в списке:', Z_MAX, 'and', Z_MAX)
else:
    for i in LIST:
        if i > Z_MAX and i < X_MAX:
            X_MAX = i
    print('Два минимальных числа в списке:', Z_MAX, 'и', X_MAX)

