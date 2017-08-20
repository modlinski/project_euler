#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:brief: Module containing solutions of Project Euler Problem 9.
:author: Michal Modlinski
:created: 19.08.2017
"""
from time import time


def triplet_1():
    count = 0
    for a in range(1, 1000):
        for b in range(a, 1000):
            c = (1000 - a - b)
            count += 1
            if a**2 + b**2 == c**2:
                return a * b * c

if __name__ == "__main__":

    start = time()
    assert triplet_1() == 31875000
    print("Time of execution for triplet: ", time() - start)
