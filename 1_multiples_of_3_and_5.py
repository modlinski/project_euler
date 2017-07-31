# !/usr/bin/env python
# encoding: utf-8
from time import time


def sum_below_1(div_1, div_2, limes):
    def sum_below(div, lim):
        num_of_multiples = int((lim - 1) / div)
        return int(div * num_of_multiples * (num_of_multiples + 1))
    return int((sum_below(div_1, limes) + sum_below(div_2, limes) - sum_below(div_1 * div_2, limes)) / 2)

assert sum_below_1(3, 5, 10) == 23
assert sum_below_1(3, 5, 1000) == 233168
start = time()
assert sum_below_1(3, 5, 1000000) == 233333166668
print("Time of execution for sum_below_1: ", time() - start)


def sum_below_2(div_1, div_2, limes):
    return sum(set(range(div_1, limes, div_1)) | set(range(div_2, limes, div_2)))

assert sum_below_2(3, 5, 10) == 23
assert sum_below_2(3, 5, 1000) == 233168
start = time()
assert sum_below_2(3, 5, 1000000) == 233333166668
print("Time of execution for sum_below_2: ", time() - start)


def sum_below_3(div_1, div_2, limes):
    sum_of_number = 0
    for num in range(1, limes):
        if num % div_1 == 0 or num % div_2 == 0:
            sum_of_number = sum_of_number + num
    return sum_of_number

assert sum_below_3(3, 5, 10) == 23
assert sum_below_3(3, 5, 1000) == 233168
start = time()
assert sum_below_3(3, 5, 1000000) == 233333166668
print("Time of execution for sum_below_3: ", time() - start)


def sum_below_4(div_1, div_2, limes):
    def sum_below():
        for i in range(limes):
            if i % div_1 == 0 or i % div_2 == 0:
                yield i
    return sum(sum_below())

assert sum_below_4(3, 5, 10) == 23
assert sum_below_4(3, 5, 1000) == 233168
start = time()
assert sum_below_4(3, 5, 1000000) == 233333166668
print("Time of execution for sum_below_4: ", time() - start)
