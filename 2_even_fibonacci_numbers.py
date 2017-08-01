#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import time

# The Fibonacci numbers are the numbers in the following integer sequence, called the Fibonacci sequence. By definition,
# the first two numbers in the Fibonacci sequence are either 1 and 1, or 0 and 1, depending on the chosen starting
# point of the sequence, and each subsequent number is the sum of the previous two. In this problem Fibonacci sequence
# is defined in different way, the first two numbers are 1 and 2, but it does not matter because only even-valued terms
# must be summed.


def sum_even_fibonacci_1(n):
    def fibonacci(m):
        if m == 1:
            return 0
        elif m == 2:
            return 1
        else:
            return fibonacci(m - 1) + fibonacci(m - 2)
    sum_even = 0
    counter = 0
    term = 0
    while term <= n:
        counter += 1
        if term % 2 == 0:
            sum_even = sum_even + term
        term = fibonacci(counter)
    return sum_even

start = time()
assert sum_even_fibonacci_1(4000000) == 4613732
print("Time of execution for sum_even_fibonacci_1: ", time() - start)


def sum_even_fibonacci_2(n):
    x = y = 1
    even_sum = 0
    while even_sum < n:
        even_sum += (x + y)
        x, y = x + 2 * y, 2 * x + 3 * y
    return even_sum

start = time()
assert sum_even_fibonacci_2(4000000) == 4613732
print("Time of execution for sum_even_fibonacci_2: ", time() - start)


def sum_even_fibonacci_3(n):
    def fibonacci_help(m):
        if m == 1:
            return 1
        elif m == 2:
            return 2
        else:
            return fibonacci_help(m - 1) + fibonacci_help(m - 2)
    sum_even = 0
    counter = 0
    term = 0
    while term <= n:
        counter += 1
        if term % 2 == 0:
            sum_even = sum_even + term
        term = fibonacci_help(counter)
    return sum_even

start = time()
assert sum_even_fibonacci_3(4000000) == 4613732
print("Time of execution for sum_even_fibonacci_3: ", time() - start)
