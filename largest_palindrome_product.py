#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:brief: Module containing solutions of Project Euler Problem 4.
:author: Michal Modlinski
:created: 16.08.2017
"""
from time import time


def palindrome_1():
    pal_num = []
    for num_1 in range(100, 999):
        for num_2 in range(100, 999):
            word = str(num_1*num_2)
            if word == word[::-1]:
                pal_num.append(int(word))
    return max(pal_num)


def palindrome_2():
    pass

if __name__ == "__main__":
    start = time()
    assert palindrome_1() == 906609
    print("Time of execution for palindrome_1: ", time() - start)
    # start = time()
    # assert palindrome_2() ==
    # print("Time of execution for palindrome_2: ", time() - start)
