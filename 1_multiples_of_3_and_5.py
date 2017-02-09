# !/usr/bin/env python
# encoding: utf-8


def sum_below(limes):
    sum_of_number = 0
    for num in xrange(1, limes):
        if num % 3 == 0 or num % 5 == 0:
            sum_of_number = sum_of_number + num
    return sum_of_number

print sum_below(10)
print sum_below(1000)
