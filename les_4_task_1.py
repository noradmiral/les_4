# Выбрана задача 1 из 3 урока

# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

import cProfile
import timeit


MAX_NUMBER = 99
MIN_DIV = 2
MAX_DIV = 9


def div_count(max_number):
    div_dict = dict()

    for div in range(MIN_DIV, MAX_DIV + 1):
        div_dict[div] = max_number // div

    return div_dict

# 4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_1.py:15(div_count)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('div_count(9999)')
# Алгоритм работает приблизительно за O(1). Т.к. при увеличении количества элементов в 10 раз на каждый запуск
#  время выполнения увеличивалось незначительно. При увеличении количества входных элементов в 1000 раз время
#  увеличилось всего на 7,5%



# Алгоритм работает быстро, в оптимизации не нуждается.


def div_count_dict(max_number):
    div_dict = dict()

    for div in range(MIN_DIV, MAX_DIV + 1):
        div_dict[div] = 0

        for num in range(2, max_number + 1):

            if num % div == 0:
                div_dict[div] += 1

    return div_dict

# 4 function calls in 0.052 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.052    0.052 <string>:1(<module>)
#         1    0.052    0.052    0.052    0.052 les_4_task_1.py:33(div_count_dict)
#         1    0.000    0.000    0.052    0.052 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('div_count_dict(99999)')
# Алгоритм работает приблизительно за O(n). Т.к. при увеличении количества элементов в 10 раз на каждый запуск
#  время выполнения увеличивается приблизительно в 10 раз.
# И даже на самом маленьком размере входных данных алгоритм работает значительно медленнее, чем div_count()



# Рекурсий в алгоритме нет, время выполнения нарастает линейно.


def div_count_xxxx(max_number):
    div_dict = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    for num in range(2, max_number + 1):

        if num % 2 == 0:
            div_dict[2] += 1

        if num % 3 == 0:
            div_dict[3] += 1

        if num % 4 == 0:
            div_dict[4] += 1

        if num % 5 == 0:
            div_dict[5] += 1

        if num % 6 == 0:
            div_dict[6] += 1

        if num % 7 == 0:
            div_dict[7] += 1

        if num % 8 == 0:
            div_dict[8] += 1

        if num % 9 == 0:
            div_dict[9] += 1

    return div_dict


# 4 function calls in 0.042 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.042    0.042 <string>:1(<module>)
#         1    0.042    0.042    0.042    0.042 les_4_task_1.py:55(div_count_xxxx)
#         1    0.000    0.000    0.042    0.042 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('div_count_xxxx(99999)')
# Алгоритм работает приблизительно за O(n). Т.к. при увеличении количества элементов в 10 раз на каждый запуск
#  время выполнения увеличивается приблизительно в 10 раз.
# И даже на самом маленьком размере входных данных алгоритм работает значительно медленнее, чем div_count(),
# при этом этот алгоритм чуть быстрее, чем div_count_dict()



# Рекурсий в алгоритме нет, время выполнения нарастает линейно.


# ВЫВОД:
# Алгоритм, использованный в функции div_count(), является самым оптимальным и быстрым.
# Так как он выполняется практически за константное время, несильно завися от размера входных данных.




print(timeit.timeit('a = [i for i in range(10)]', globals=globals(), number=1000)) #0.0004564999835565686
print(timeit.timeit('a = [i for i in range(100)]', globals=globals(), number=1000)) #0.0021436000242829323
print(timeit.timeit('a = [i for i in range(1000)]', globals=globals(), number=1000)) #0.022245199885219336
print(timeit.timeit('a = [i for i in range(10000)]', globals=globals(), number=1000)) #0.19941260002087802
print(timeit.timeit('a = [i for i in range(100000)]', globals=globals(), number=1000)) #2.9502418000483885
# print(div_count(MAX_NUMBER))
# print(div_count_dict(MAX_NUMBER))
# print(div_count_xxxx(MAX_NUMBER))
