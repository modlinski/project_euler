#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:brief: Module containing solutions of Project Euler Problem 4.
:author: Michal Modlinski
:created: 16.08.2017
"""
from time import time


def palindrome_1():
    max_p = 0
    for num_1 in range(100, 1000):
        for num_2 in range(num_1, 1000):
            p = num_1 * num_2
            if p > max_p:
                if str(p) == str(p)[::-1]:
                    max_p = p
    return max_p


def palindrome_2():
    # The palindrome can be written as 100000a + 10000b + 1000c + 100c + 10b + a, which can be simplified to
    # 11(9091a + 910b + 100c), so at least one of the numbers must be divisible by 11.
    maximum = 0
    num_1 = 999
    while num_1 > 100:
        num_2 = 990
        while num_2 > 100:
            product = num_1 * num_2
            if product > maximum:
                product_string = str(product)
                if product_string == product_string[::-1]:
                    maximum = product
            num_2 -= 11
        num_1 -= 1
    return maximum

if __name__ == "__main__":
    start = time()
    assert palindrome_1() == 906609
    print("Time of execution for palindrome_1: ", time() - start)
    start = time()
    assert palindrome_2() == 906609
    print("Time of execution for palindrome_2: ", time() - start)
