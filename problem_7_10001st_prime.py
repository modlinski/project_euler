#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:brief: Module containing solutions of Project Euler Problem 7.
:author: Michal Modlinski
:created: 19.08.2017
"""
from time import time
from math import floor, sqrt


def prime_1(n):
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
    counter = 1
    candidate = 1
    while counter < n:
        candidate += 2
        if is_prime(candidate):
            counter += 1
    return candidate


def prime_2(n):
    can = 3
    primes = [2]
    while len(primes) < n:
        flag = True
        for i in primes:
            if can % i == 0:
                flag = False
                break
        if flag:
            primes.append(can)
        can += 1
    return primes[-1]

if __name__ == "__main__":
    start = time()
    assert prime_1(10001) == 104743
    print("Time of execution for prime_1: ", time() - start)
    start = time()
    assert prime_2(10001) == 104743
    print("Time of execution for prime_2: ", time() - start)
