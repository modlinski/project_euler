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
    for num_1 in range(100, 1000):
        for num_2 in range(num_1, 1000):
            word = str(num_1*num_2)
            if word == word[::-1]:
                pal_num.append(int(word))
    return max(pal_num)


def palindrome_2():
    # The palindrome can be written as 100000a + 10000b + 1000c + 100c + 10b + a which can be simplified to
    # 11(9091a + 910b + 100c), so at least one of the numbers must be divisible by 11.
    maximum = 0
    i = 999
    while i > 100:
        j = 990
        while j > 100:
            product = i * j
            if product > maximum:
                product_string = str(product)
                if product_string == product_string[::-1]:
                    maximum = product
            j -= 11
        i -= 1
    return maximum


def palindrome_3():
    max_p = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            p = i * j
            if p > max_p:
                if str(p) == str(p)[::-1]:
                    max_p = p
    return max_p

if __name__ == "__main__":
    start = time()
    assert palindrome_1() == 906609
    print("Time of execution for palindrome_1: ", time() - start)
    start = time()
    assert palindrome_2() == 906609
    print("Time of execution for palindrome_2: ", time() - start)
    start = time()
    assert palindrome_3() == 906609
    print("Time of execution for palindrome_3: ", time() - start)

# max([x*y for x in range(900,1000) for y in range(900,1000) if str(x*y) == str(x*y)[::-1]])
#
# son=0
# for a in range(999,99,-1):
#     for b in range(999,99,-1):
#                 c=a*b
#                 d=len(str(c))
#                 e=list(str(c)[0:d/2])
#                 f=list(str(c)[d/2:])
#                 f.reverse()
#                 if e==f:
#                     if c>son:
#                         son=c
#                         print c,a,b
#                     else:
#                         pass
#                 else :
#                     pass
#
# def main():
#     # Brute force, but backward because we need the max_imum - found all palindromes starting at 9998001 (999^2), and
#     # checked each to see if it was divisible by a 3 digit number, starting at 999.
#     for i in range(999999,99999,-1):
#         if str(i) == str(i)[::-1]:
#             for j in range(999,99,-1):
#                 if (i % j == 0) and (i / j < 1000):
#                     return i
