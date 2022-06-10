# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 22:01:33 2022

@author: a403922
"""

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import math
import numpy as np

#Wilson's theorem states that a natural number n+1 is prime if and only if
#n!=n mod (n+1)

def wilsons_thm(y):
    n=y-1
    if (math.factorial(n)-n)%y==0:
        return True
    else:
        return False
    
def largest_prime(x):
    for i in range(int(np.sqrt(x)),1,-1):
    
        if x%i==0 and wilsons_thm(i):   
            return i
    return 1

def largest_prime2(x):
    a=1
    while a**2<x:
        while x%a==0:
            x=x/a
        a+=1
    return x




        
        