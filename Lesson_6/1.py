"""Профилировка затрат памяти"""

import memory_profiler


@memory_profiler.profile
def eratosfen_prime_numbers(limit=10000, position=500):
    """
   Функция находит ряд простых чисел до i-ого элемента включительно и возвращает весь ряд чисел.
   Для нахождения используем алгоритм "Решето Эратосфена".
   """
    n = 2
    list_1 = list(range(limit + 1))

    list_1[1] = 0
    while n < limit:
        if list_1[n] != 0:
            m = n * 2
            while m < limit:
                list_1[m] = 0
                m += n
        n += 1
    result = [p for p in list_1 if p != 0][position]
    return result


@memory_profiler.profile
def non_eratosfen(position=500):
    x = 0
    i = 2
    list1 = [2]
    while x < position:  # до тех пор пока простое число по счету не стало равным искомому числу( последовательности)
        i += 1
        j = 2
        while j < i:
            if i % j == 0:
                break
            else:
                j += 1
        else:
            list1.append(i)
            x += 1
    return list1[position]


if __name__ == "__main__":
    m1 = memory_profiler.memory_usage()
    eratosfen_memory = eratosfen_prime_numbers()
    m2 = memory_profiler.memory_usage()
    mem_diff = m2[0] - m1[0]
    print(f"Выполнение через решето заняло:  {mem_diff} Мб")

    m1 = memory_profiler.memory_usage()
    oneratosfen_memory = non_eratosfen()
    m2 = memory_profiler.memory_usage()
    mem_diff = m2[0] - m1[0]

    print(f"Выполнение без использования решета заняло: {mem_diff} Мб")

'''
При использовании решета, очевидно что выделение памяти будет больше. 
Чем больше массив тем больше будет отрыв по памяти от наивного решения
Из-за того что наивное решение формирует массив по факту рассчета простых чисел а не сразу грузит в память -
получается быстрее. 

Повторил эту упражнение на нескольких задачах, везде выделение памяти шло только на формирование массива  
на другие части кода потребления нигде я не нашел. 

64 разрядная win10 
Python 3.8

Line #    Mem usage    Increment   Line Contents
================================================
     8     13.5 MiB     13.5 MiB   @memory_profiler.profile
     9                             def eratosfen_prime_numbers(limit=10000, position=500):
    10                                 """
    11                                Функция находит ряд простых чисел до i-ого элемента включительно и возвращает весь ряд чисел.
    12                                Для нахождения используем алгоритм "Решето Эратосфена".
    13                                """
    14     13.5 MiB      0.0 MiB       n = 2
    15     13.7 MiB      0.2 MiB       list_1 = list(range(limit + 1))
    16                             
    17     13.7 MiB      0.0 MiB       list_1[1] = 0
    18     13.7 MiB      0.0 MiB       while n < limit:
    19     13.7 MiB      0.0 MiB           if list_1[n] != 0:
    20     13.7 MiB      0.0 MiB               m = n * 2
    21     13.7 MiB      0.0 MiB               while m < limit:
    22     13.7 MiB      0.0 MiB                   list_1[m] = 0
    23     13.7 MiB      0.0 MiB                   m += n
    24     13.7 MiB      0.0 MiB           n += 1
    25     13.7 MiB      0.0 MiB       result = [p for p in list_1 if p != 0][position]
    26     13.7 MiB      0.0 MiB       return result


Выполнение через решето заняло:  0.35546875 Мб
Filename: C:/Users/Peoplecanfly/PycharmProjects/untitled/venv/Lesson6_memory/1.py

Line #    Mem usage    Increment   Line Contents
================================================
    29     13.7 MiB     13.7 MiB   @memory_profiler.profile
    30                             def non_eratosfen(position=500):
    31     13.7 MiB      0.0 MiB       x = 0
    32     13.7 MiB      0.0 MiB       i = 2
    33     13.7 MiB      0.0 MiB       list1 = [2]
    34     13.8 MiB      0.0 MiB       while x < position:  # до тех пор пока простое число по счету не стало равным искомому числу( последовательности)
    35     13.8 MiB      0.0 MiB           i += 1
    36     13.8 MiB      0.0 MiB           j = 2
    37     13.8 MiB      0.0 MiB           while j < i:
    38     13.8 MiB      0.0 MiB               if i % j == 0:
    39     13.8 MiB      0.0 MiB                   break
    40                                         else:
    41     13.8 MiB      0.0 MiB                   j += 1
    42                                     else:
    43     13.8 MiB      0.0 MiB               list1.append(i)
    44     13.8 MiB      0.0 MiB               x += 1
    45     13.8 MiB      0.0 MiB       return list1[position]


Выполнение без использования решета заняло: 0.05078125 Мб
'''