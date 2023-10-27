# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 13:01:44 2023

@author: Joanna.Guziwelakis
"""

'''
Finger exercise: Write a list comprehension that generates all non-primes be
tween 2 and 100.

'''
# przykład z książki
# print([x for x in range(2, 100) if all (x % y != 0 for y in range(3, x))])

# # rozwiązanie zadania
# l=[x for x in range(2,100) if all( x%2==0 or x%y==0 for y in range(3, 2, x))]
# print(l)



# l=[x for x in range(2,100) if any( x!=y and x%y==0 for y in range(2, x))]
# print(l)

l=[x for x in range(2,100) if any(  x%y==0 and x!=y for y in range(2,x) )]
print(l)