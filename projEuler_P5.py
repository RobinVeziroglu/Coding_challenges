# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 12:27:06 2022

@author: a403922
"""

def smallest_multiple():
    n=2520
    lst=[20,19,18,17,16,15,14,13,11]
    while True:
        if all([n%t==0 for t in lst]):
            return n
        n+=2520
    
if __name__=="__main__":
    print(smallest_multiple())