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
    for num in range(6, ceiling + 1, 6):
        candidate_1 = num - 1
        candidate_2 = num + 1
        if is_prime(candidate_1):
            sum_of_primes += candidate_1
        if is_prime(candidate_2):
            sum_of_primes += candidate_2
    return sum_of_primes

if __name__ == "__main__":
    start = time()
    assert summation_1(2000000) == 142913828922
    print("Time of execution for summation_1: ", time() - start)
