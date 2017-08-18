#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:brief: Module containing solutions of Project Euler Problem 5.
:author: Michal Modlinski
:created: 16.08.2017
"""
from time import time
from functools import reduce


def least_common_multiple_1(divisors):
    number = 1
    for k in divisors:
        if number % k > 0:
            for j in divisors:
                if (number*j) % k == 0:
                    number *= j
                    break
    return number


def least_common_multiple_2(divisors):

    def greatest_common_divisor(a, b):
        while b:
            a, b = b, a % b
        return a

    def least_common_multiple(a, b):
        return a * b / greatest_common_divisor(a, b)

    return reduce(least_common_multiple, divisors, 1)


def least_common_multiple_3(n):

    result = 1

    def greatest_common_divisor(a, b):
        while b:
            a, b = b, a % b
        return a

    def least_common_multiple(a, b):
        return a * b / greatest_common_divisor(a, b)

    for num in range(2, n+1):
        result = least_common_multiple(num, result)

    return result


def least_common_multiple_4(n):
    result = 1
    for div in range(2, n+1):
        multiplier = 1
        product = result
        while product % div != 0:
            multiplier += 1
            product = result * multiplier
        result = product
    return result


def least_common_multiple_5(number):

    def check_div(t, n):
        if n > 0:
            if not (t % n):
                if check_div(t, n - 1):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return True

    product = number
    while not check_div(product, number):
        product += number
    return product


if __name__ == "__main__":

    start = time()
    assert least_common_multiple_1(range(1, 21)) == 232792560
    print("Time of execution for least_common_multiple_1: ", time() - start)

    start = time()
    assert least_common_multiple_2(range(1, 21)) == 232792560
    print("Time of execution for least_common_multiple_2: ", time() - start)

    start = time()
    assert least_common_multiple_3(20) == 232792560
    print("Time of execution for least_common_multiple_3: ", time() - start)

    start = time()
    assert least_common_multiple_4(20) == 232792560
    print("Time of execution for least_common_multiple_4: ", time() - start)

    start = time()
    assert least_common_multiple_5(20) == 232792560
    print("Time of execution for least_common_multiple_5: ", time() - start)
