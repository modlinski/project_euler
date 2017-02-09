#!/usr/bin/env python
# -*- coding: utf-8 -*-


def largest_prime_factor(number):
    factors = []
    for i in xrange(1, number):
        if number % i == 0:
            factors.append(i)
    return factors

# print largest_prime_factor(100)

prime_factors = []


def rec(n):
    for i in xrange(2, n+1):
        print '-----' + str(i) + '-----'
        if n % i == 0 and n != i:
            print 'dziele przez: ' + str(i)
            print 'zostaje mi: ' + str(n/i)
            prime_factors.append(i)
            n = n/i
            return rec(n)
        elif n == i:
            print 'ostatni: ' + str(i)
            prime_factors.append(i)
            # return rec(n)

# print rek(11*11*11*2*3*2)
# print rek(13195)
rec(600851475143)
print prime_factors
