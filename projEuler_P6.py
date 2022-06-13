# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 13:19:50 2022

@author: a403922
"""

def sum_sq_difference(n):
    lst1=[x**2 for x in range(1,n+1)]
    lst2=[x for x in range(1,n+1)]
    return f"The difference between the sum of the squares of the first {n} natural numbers and the square of the sum is equal to: {sum(lst2)**2-sum(lst1)}"

if __name__=="__main__":
    print(sum_sq_difference(100))