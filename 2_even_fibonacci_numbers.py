#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def sum_even_fibonacci(n):
    sum_even = 0
    counter = 0
    term = 0
    while term <= n:
        counter += 1
        if term % 2 == 0:
            sum_even = sum_even + term
        term = fibonacci(counter)
    return sum_even


print sum_even_fibonacci(4000000)
