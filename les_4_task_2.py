# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Второй — без использования «Решета Эратосфена».

# Тестовая функция проверяет до 1229-го простого числа.

import cProfile
import timeit

def test(num, n=10000):
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]
    print(f'Количество простых чисел в диапазоне до {n}: {len(res)}')

    assert num < len(res)
    return res[num - 1]


def eratosthenes_sieve(n):
    count = 1
    start = 3
    end = 4 * n

    sieve = [i for i in range(start, end) if i % 2 != 0]
    prime = [2]

    if n == 1:
        return 2

    while count < n:

        for i in range(len(sieve)):

            if sieve[i] != 0:
                count += 1

                if count == n:
                    return sieve[i]

                j = i + sieve[i]

                while j < len(sieve):
                    sieve[j] = 0
                    j += sieve[i]

        prime.extend([i for i in sieve if i != 0])

        start, end = end, end + 2 * n
        sieve = [i for i in range(start, end) if i % 2 != 0]

        for i in range(len(sieve)):

            for num in prime:

                if sieve[i] % num == 0:
                    sieve[i] = 0
                    break


# Предположительно, алгоритм сложности O(n**2). Увеличение количества чисел в 10 раз
# увеличивает время выполнения приблизительно в 100 раз

cProfile.run('eratosthenes_sieve(10)')
# 27 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:31(eratosthenes_sieve)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:36(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        22    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('eratosthenes_sieve(100)')
# 353 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:31(eratosthenes_sieve)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:36(<listcomp>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:58(<listcomp>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:61(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       345    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
cProfile.run('eratosthenes_sieve(1000)')
# 4289 function calls in 0.018 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.018    0.018 <string>:1(<module>)
#         1    0.017    0.017    0.018    0.018 les_4_task_2.py:31(eratosthenes_sieve)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:36(<listcomp>)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:58(<listcomp>)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:61(<listcomp>)
#         1    0.000    0.000    0.018    0.018 {built-in method builtins.exec}
#      4278    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         2    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
# Время выполнения нарастает. Рекурсий нет.


def search_prime(n):
    count = 1
    number = 1
    prime = [2]

    if n == 1:
        return 2

    while count != n:
        number += 2

        for num in prime:
            if number % num == 0:
                break
        else:
            count += 1
            prime.append(number)

    return number


# Сложность близка к O(n**2)
# Скорость работы обоих алгоритмов на данных объемах данных практически одинакова.

cProfile.run('search_prime(1000)')
# 1003 function calls in 0.024 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.024    0.024 <string>:1(<module>)
#         1    0.024    0.024    0.024    0.024 les_4_task_2.py:91(search_prime)
#         1    0.000    0.000    0.024    0.024 {built-in method builtins.exec}
#       999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# Время выполнения нарастает. Рекурсий нет.


# ВЫВОД:
# Сложность алгоритмов и время их работы приблизительно одинаковые.


n = 521

# if eratosthenes_sieve(n) == test(n):
#     print(f'{n}-ое простое число {eratosthenes_sieve(n)}')
#     print('OK')
# else:
#     print('Ошибка')

# if search_prime(n) == test(n):
#     print(f'{n}-ое простое число {search_prime(n)}')
#     print('OK')
# else:
#     print('Ошибка')