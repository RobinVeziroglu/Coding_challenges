# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 22:01:33 2022

@author: a403922
"""

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''


def largest_prime(x):
    for i in range(x-1,1,-1):
        if x%i==0 and all(i%j!=0 for j in range(2,i)):
            return i
    return 1