#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:brief: Module containing solutions of Project Euler Problem 7.
:author: Michal Modlinski
:created: 19.08.2017
"""
from time import time


def prime(n):
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


def prime_2(n):
    i = 3
    n = s = 1
    while (i <= 10001):
            if s == 1:
                x = 6 * n - 1
                s = 0
            else:
                x = 6 * n + 1
                s = 1
                n = n + 1
            r = x ** .5
            p = 1
            t = 3
            while t <= r:
                if x % t == 0:
                    p = 0
                t = t + 2
            if p == 1:
                i = i + 1
    return x


if __name__ == "__main__":
    start = time()
    assert prime(10001) == 104743
    print("Time of execution for prime: ", time() - start)
    start = time()
    assert prime_2(10001) == 104743
    print("Time of execution for prime: ", time() - start)
