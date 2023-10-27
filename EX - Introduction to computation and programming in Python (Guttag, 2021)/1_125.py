# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 18:47:17 2023

@author: Joanna.Guziwelakis
"""

'''

Finger exerCise The harmonic sum of an integer, n > 0, can be calculated using
the formula 1 +1/2+1/3 + ...+ 1/n Write a recursive function that computes this.

'''

def harmonic_sum(n):
    if n==1:
       return 1
    else:
      ans=harmonic_sum(n-1) +(1/n)
      return ans
    
n=int(input('insert integer >0 n '))

print('harmonic_sum',n,') =', harmonic_sum(n))
    
