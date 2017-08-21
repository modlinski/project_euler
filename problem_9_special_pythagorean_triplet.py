#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:brief: Module containing solutions of Project Euler Problem 9.
:author: Michal Modlinski
:created: 19.08.2017
"""
from time import time
from math import floor


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

if __name__ == "__main__":
    start = time()
    assert triplet_1(1000) == 31875000
    print("Time of execution for triplet_1: ", time() - start)
    start = time()
    assert triplet_2(1000) == 31875000
    print("Time of execution for triplet_2: ", time() - start)
