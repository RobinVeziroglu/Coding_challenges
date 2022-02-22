# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 17:41:54 2022

@author: a403922
"""

#Problem 1

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
#The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.

def mult_3_5(x):
    lst=[y for y in range(1,x) if y%3==0 or y%5==0]
    return "The sum of all the multiples of 3 or 5 below {} is equal to {}.".format(x,sum(lst))

if __name__=="__main__":
    print(mult_3_5(10))
    print(mult_3_5(1000))