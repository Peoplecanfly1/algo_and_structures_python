"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

LIST1 = []
LIST2 = []

for i in range(2, 100):
    LIST1.append(i)

for x in range(2, 10):
    LIST2.append(x)

for i in LIST2:
    n = 0
    for j in LIST1:
        if j % i == 0:
            n += 1
    print(i, ':', n)
