#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:brief: Module containing solutions of Project Euler Problem 8.
:author: Michal Modlinski
:created: 19.08.2017
"""
from time import time
from functools import reduce
from string import whitespace
from operator import mul


def largest_product_1(n, input_series):
    product = 1
    n_of_zeros = 0
    for num in input_series[0:n]:
        if num == 0:
            n_of_zeros += 1
        else:
            product *= int(num)
    maximum = product if n_of_zeros == 0 else 0
    for index in range(len(input_series) - n):
        if int(input_series[index]) != 0:
            product /= int(input_series[index])
        else:
            n_of_zeros -= 1
        if int(input_series[index + n]) != 0:
            product *= int(input_series[index+n])
        else:
            n_of_zeros += 1
        maximum = max(maximum, product if n_of_zeros == 0 else 0)
    return maximum


def largest_product_2(n, input_series):
    nos = [int(c) for line in input_series for c in line if c not in whitespace]
    return max([reduce(mul, nos[i:i + n]) for i in range(len(nos) - n)])

if __name__ == "__main__":

    series = "731671765313306249192251196744265747423553491949349698352031277450632623957831801698480186947885184385861" \
             "560789112949495459501737958331952853208805511125406987471585238630507156932909632952274430435576689664895" \
             "044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749303589072962904" \
             "915604407723907138105158593079608667017242712188399879790879227492190169972088809377665727333001053367881" \
             "220235421809751254540594752243525849077116705560136048395864467063244157221553975369781797784617406495514" \
             "929086256932197846862248283972241375657056057490261407972968652414535100474821663704844031998900088952434" \
             "506585412275886668811642717147992444292823086346567481391912316282458617866458359124566529476545682848912" \
             "883142607690042242190226710556263211111093705442175069416589604080719840385096245544436298123098787992724" \
             "428490918884580156166097919133875499200524063689912560717606058861164671094050775410022569831552000559357" \
             "2972571636269561882670428252483600823257530420752963450"

    start = time()
    assert largest_product_1(13, series) == 23514624000
    print("Time of execution for largest_product_1: ", time() - start)
    start = time()
    assert largest_product_2(13, series) == 23514624000
    print("Time of execution for largest_product_2: ", time() - start)
