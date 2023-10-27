# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 19:18:17 2023

@author: Joanna.Guziwelakis
"""

"""Finger exercise: Use the find_root function in Figure 4-3 to print the sum of ap
proximations to the square root of 25, the cube root of -8, and the fourth root of
16. Use 0.00 1 as epsilon


def find_root(x, power, epsilon):
# Find interval containing answer
    if x < 0 and power%2 == 0:
        return None #Negative number has no even-powered roots
    low = min(-1, x)
    high = max(1, x)
    #Use bisection search
    ans = (high + low)/2
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans (high + low)/2
    return ans

"""

# """Finger exercise: Use the find_root function in Figure 4-3 to print the sum of ap
# proximations to the square root of 25, the cube root of -8, and the fourth root of
# 16

def find_root(x, power, epsilon):

    if x < 0 and power%2 == 0:
        return None 
    low = min(-1, x)
    high = max(1, x)
    
    ans = (high + low)/2
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans=(high + low)/2
    return ans
epsilon=0.001
suma=0
for z in range(0,3):
    
    power=int(input("potęga"))
    x=int(input("x="))
    
    suma=find_root(x, power, epsilon)+suma
    
print(suma)