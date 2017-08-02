#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:brief: Module containing solutions of Project Euler Problem 2.
:author: Michal Modlinski
:created: 02.08.2017
"""
from time import time


# The Fibonacci numbers are the numbers in the following integer sequence, called the Fibonacci sequence. By definition,
# the first two numbers in the Fibonacci sequence are either 1 and 1, or 0 and 1, depending on the chosen starting point
# of the sequence, and each subsequent number is the sum of the previous two. In this problem Fibonacci sequence is
# defined in different way, the first two numbers are 1 and 2, but it does not matter because only even-valued terms
# must be summed.


def sum_even_fibonacci_1(maximum):
    x = 1
    y = 2
    even_sum = 0
    while even_sum < maximum:
        even_sum += y
        x, y = x + 2 * y, 2 * x + 3 * y
    return even_sum


def sum_even_fibonacci_2(maximum):
    def generate(ceiling):
        a, b = 1, 2
        while a < ceiling:
            yield a
            a, b = b, a + b
    result = 0
    for n in generate(maximum):
        if n % 2 == 0:
            result += n
    return result


def sum_even_fibonacci_3(maximum):
    def fibonacci(m):
        if m == 1:
            return 1
        elif m == 2:
            return 2
        else:
            return fibonacci(m - 1) + fibonacci(m - 2)
    sum_even = 0
    counter = 0
    term = 0
    while term <= maximum:
        counter += 1
        if term % 2 == 0:
            sum_even = sum_even + term
        term = fibonacci(counter)
    return sum_even


if __name__ == "__main__":
    start = time()
    assert sum_even_fibonacci_1(4000000) == 4613732
    print("Time of execution for sum_even_fibonacci_1: ", time() - start)
    start = time()
    assert sum_even_fibonacci_2(4000000) == 4613732
    print("Time of execution for sum_even_fibonacci_2: ", time() - start)
    start = time()
    assert sum_even_fibonacci_3(4000000) == 4613732
    print("Time of execution for sum_even_fibonacci_3: ", time() - start)
