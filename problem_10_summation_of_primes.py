#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:brief: Module containing solutions of Project Euler Problem 10.
:author: Michal Modlinski
:created: 25.08.2017
"""
from time import time


def summation_1(ceiling):
    for num in range(6, ceiling + 1, 6):
        print(num - 1)
        print(num + 1)

if __name__ == "__main__":
    start = time()
    # assert summation_1(2000000) ==
    # print(summation_1(2000000))
    print(summation_1(200))
    print("Time of execution for summation_1: ", time() - start)
