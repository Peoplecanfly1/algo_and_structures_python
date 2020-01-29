import random

m = int(input("Введите m: "))
massive = [random.randint(1, 100) for j in range(m * 2 + 1)]


def parts(array):
    left = []
    right = []
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] > array[j]:
                left.append(array[j])
            if array[i] < array[j]:
                right.append(array[j])
            if array[i] == array[j] and i > j:
                left.append(array[j])
            if array[i] == array[j] and i < j:
                right.append(array[j])
        if len(left) == len(right):
            return array[i]
        left.clear()
        right.clear()


print(massive)
print(parts(massive))