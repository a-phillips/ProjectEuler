#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:04:04 2020

@author: aphillips
"""

def prime_sieve(n):
    sieve = [0] * n
    primes = []
    for i in range(2, len(sieve)):
        if sieve[i] == 0:
            primes.append(i)
            inc = i
            while i < len(sieve):
                sieve[i] = 1
                i += inc
    return primes

def smallest_mult(n):
    primes = prime_sieve(n)
    mult = 1
    for i in range(len(primes)):
        exp = 1
        while (primes[i] ** exp) < n:
            exp += 1
        mult *= (primes[i] ** (exp - 1))
    return mult

if __name__ == '__main__':
    print(smallest_mult(20))