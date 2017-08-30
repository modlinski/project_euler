#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:brief: Module containing solutions of Project Euler Problem 9.
:author: Michal Modlinski
:created: 19.08.2017
"""
from time import time
from math import floor, sqrt


def triplet_1(s):
    for a in range(1, s):
        for b in range(a, s):
            c = (s - a - b)
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c


def triplet_2(s):
    # Conditions:
    # a < b < c
    # a =< (s − 3) / 3
    # b < (s − a) / 2
    for a in range(3, 1 + floor((s - 3) / 3)):
        for b in range(a + 1, floor((s - 1 - a) / 2)):
            c = (s - a - b)
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c


def triplet_3(s):
    # Conditions:
    # if greatest_common_divisor(a, b, c) == 1 then triplet a, b, c is called primitive
    # triplet a, b, c is primitive only if gcd(a, b) = 1
    # all primitive triplets (a, b, c) can be represented as:
    # a = m  ** 2 − n ** 2
    # b = 2 * m * n
    # c = m ** 2 + n ** 2
    # and:
    # m > n > 0 -> a < b
    # exactly one of m, n is even
    # greatest_common_divisor(m, n) = 1
    # from any Pythagorean triplet you get a primitive one by dividing out the greatest common divisor, so every
    # Pythagorean triplet has a unique representation:
    # a = (m ** 2 − n ** 2) * d
    # b = 2 * m * n * d
    # c = (m ** 2 + n ** 2) * d
    # and:
    # m > n > 0 -> a < b
    # exactly one of m, n is even
    # greatest_common_divisor(m, n) = 1
    # greatest_common_divisor(a, b, c) = d
    # Using that parametrisation:
    # s = a + b + c = 2 * m * (m + n) * d
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    result = []
    s_2 = s/2
    for m in range(2, floor(sqrt(s_2))):
        if s_2 % m == 0:
            s_m = s_2 / m
            # reduce the search space by removing all factors 2
            while s_m % 2 == 0:
                s_m /= 2
            if m % 2 == 1:
                k = m + 2
            else:
                k = m + 1
            while k < 2 * m and k <= s_m:
                if s_m % k == 0 and gcd(k, m) == 1:
                    d = s_2 / (k * m)
                    n = k - m
                    a = d * (m * m - n * n)
                    b = 2 * d * m * n
                    c = d * (m * m + n * n)
                    result.append((a, b, c))
                k += 2
    # return result  # for cases where more than triplet is correct value
    product = 1
    for num in result[0]:
        product *= num
    return product

if __name__ == "__main__":
    start = time()
    assert triplet_1(1000) == 31875000
    print("Time of execution for triplet_1: ", time() - start)
    start = time()
    assert triplet_2(1000) == 31875000
    print("Time of execution for triplet_2: ", time() - start)
    start = time()
    assert triplet_3(1000) == 31875000
    print("Time of execution for triplet_3: ", time() - start)
