# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 09:59:39 2022

@author: a403922
"""

def largest_palindrome(n):
    lst=[[i*j,f"{i},{j}"] for i in range(10**(n-1),10**(n)+1) for j in range(10**(n-1),10**(n)+1) if str(i*j)==str(i*j)[::-1]]
    max_pair=max(lst,key=lambda x: x[0])
    max_palondricNumber=max_pair[0]
    max_prod=max_pair[1].split(",")
    return f"The largest palindromic number made from the product of two {n}-digit numbers is {max_palondricNumber}={max_prod[0]}*{max_prod[1]}"
    

if __name__=="__main__":
    print(largest_palindrome(3))