'''
Определить, какое число в массиве встречается чаще всего.
'''

import random
import collections

N = 10
LIST = [random.randint(1, 30) for i in range(N)]
print(LIST)

print(max(set(LIST), key=LIST.count))
