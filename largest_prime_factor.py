#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:brief: Module containing solutions of Project Euler Problem 3.
:author: Michal Modlinski
:created: 04.08.2017
"""
from time import time
import itertools
from math import sqrt


def largest_prime_factor_1(number):
    beg = 2
    for num in itertools.count(beg):
        if number % num == 0:
            if num == number:
                return int(number)
            return largest_prime_factor_1(number/num)


def largest_prime_factor_2(number):
    num = 1
    while num < sqrt(number):
        num += 1
        if num > sqrt(number):
            return int(number)
        if number % num == 0:
            return largest_prime_factor_2(number/num)


def largest_prime_factor_3(number):
    product = 1
    div = 2
    new = number
    while product != number:
        if new % div == 0:
            new /= div
            product *= div
        div += 1
    return div-1

if __name__ == "__main__":
    start = time()
    assert largest_prime_factor_1(600851475143) == 6857
    print("Time of execution for largest_prime_factor_1: ", time() - start)
    start = time()
    assert largest_prime_factor_2(600851475143) == 6857
    print("Time of execution for largest_prime_factor_2: ", time() - start)
    start = time()
    assert largest_prime_factor_3(600851475143) == 6857
    print("Time of execution for largest_prime_factor_3: ", time() - start)
