#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:brief: Module containing solutions of Project Euler Problem 10.
:author: Michal Modlinski
:created: 25.08.2017
"""
from time import time
from math import floor, sqrt


def summation_1(ceiling):
    def is_prime(m):
        if m == 1:
            return False
        else:
            if m < 4:
                return True
            else:
                if m % 2 == 0:
                    return False
                else:
                    if m < 9:
                        return True
                    else:
                        if m % 3 == 0:
                            return False
                        else:
                            r = floor(sqrt(m))
                            f = 5
                            while f <= r:
                                if m % f == 0:
                                    return False
                                if m % (f + 2) == 0:
                                    return False
                                f += 6
                            else:
                                return True
    sum_of_primes = 2 + 3
    num = 5
    while num <= ceiling:
        if is_prime(num):
            sum_of_primes += num
        num += 2
        if num <= ceiling and is_prime(num):
            sum_of_primes += num
        num += 4
    return sum_of_primes


def summation_2(ceiling):
    # The sieve of Eratosthenes
    reduced_ceiling = floor(sqrt(ceiling))
    numbers = list(range(2, ceiling + 1))
    numbers.insert(0, False)
    numbers.insert(0, False)
    for even in range(4, ceiling + 1, 2):
        numbers[even] = False
    for num in range(3, reduced_ceiling + 1, 2):
        if numbers[num]:
            for m in range(num*num, ceiling + 1, 2 * num):
                numbers[m] = False
    return sum(numbers)

if __name__ == "__main__":
    start = time()
    assert summation_1(2000000) == 142913828922
    print("Time of execution for summation_1: ", time() - start)
    start = time()
    assert summation_2(2000000) == 142913828922
    print("Time of execution for summation_2: ", time() - start)
