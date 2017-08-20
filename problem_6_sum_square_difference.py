#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:brief: Module containing solutions of Project Euler Problem 6.
:author: Michal Modlinski
:created: 16.08.2017
"""
from time import time


def difference_1(n):
    return sum(list(range(1, n + 1))) ** 2 - sum([x ** 2 for x in range(1, n + 1)])


def difference_2(n):
    sum_num = n * (n + 1) / 2
    sum_sqr = (2 * n + 1) * (n + 1) * n / 6
    return sum_num ** 2 - sum_sqr

if __name__ == "__main__":

    start = time()
    assert difference_1(100) == 25164150
    print("Time of execution for least_common_multiple_1: ", time() - start)
    start = time()
    assert difference_2(100) == 25164150
    print("Time of execution for least_common_multiple_2: ", time() - start)
