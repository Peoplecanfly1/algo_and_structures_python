'''
1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
'''


import timeit

# Через цикл.
def funct_1(number):
    reuslt = ''
    while number != 0:
        x = str(number % 10)
        number = number // 10
        reuslt = reuslt + x
    return

print(timeit.timeit('funct_1(561212313124124123124123123141231)', setup="from __main__ import funct_1", number=5))


# Через рекурскию.
def versa_numbers(number, result=''):
    if number == 0:
        return
    else:
        num1 = str(number % 10)
        number = number // 10
        result = result + num1
        versa_numbers(number, result)


print(timeit.timeit('versa_numbers(561212313124124123124123123141231)', setup="from __main__ import versa_numbers", number=5 ))

'''
При использовании рекурсии, время увеличивается. 
Но на малых числах это не заметно, только при очень больших  числах становится заметна разница.

Могу предположить что сложность у них одинаковая O(n)  просто из-за рекурсивного подхода медленнее второй вариант
 

'''