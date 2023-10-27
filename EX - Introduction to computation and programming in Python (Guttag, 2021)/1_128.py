# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 19:13:37 2023

@author: Joanna.Guziwelakis
"""

'''
Finger exercise: When the implementation of fib in Figure 6-3 is used to com
pute fib(5), how many times does it compute the value of fib(2) on the way to
computing fib(5)? 

#IMO - 2





'''


def fib(n):
    '''““Assumes n mt >= 0
    Returns Fibonacci of n”’”'''
   
    if n == 0 or n == 1:
        return 1
    else:
        ans=(fib(n-1) + fib(n-2))

        if n-1==2 :
            
            print('użyciefib(2)')
        if n-2==2:   
            print('użyciefib(2)')
    return ans
n=int(input('insert integer >0 n '))


print('f= ',fib(n))

# def test_f ib(n):
#     for i in range(n+1):
#         print(’fib of’, i, ‘=‘, fib(i))