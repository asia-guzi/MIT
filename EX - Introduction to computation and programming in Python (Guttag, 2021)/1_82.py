# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 16:49:50 2023

@author: Joanna.Guziwelakis
"""

# Finger exercise: Using the algorithm of Figure 3-6, write a function that satisfies
# the specification
# def log(x, base, epsilon):
# Assumes x and epsilon mt or float, base an int,
# x > 1, epsilon > 0 & power >= 1
# Returns float y such that base**y is within epsilon o-f x.



# # Find lower bound on ans
# lower_bound = 0
# while 2**lower_bound < x:
#     lower_bound += 1
#     low = lower_bound - 1
#     high = lower_bound + 1
# # Perform bisection search
# ans = (high + low)/2
# while abs(2**ans - x) >= epsilon:
#     if 2**ans < x:
#             low = ans
#     else:
#             high = ans
#     ans = (high + low)/2
# print(ans, 'is close to the log base 2 of', x)


 
def log(x, base, epsilon):
    
    '''
     Assumes x and epsilon int or float, base an int,
    
    Returns float y such that base**y is within epsilon of x.
    
    '''


    lower_bound = 0
    while base**lower_bound < x:
        lower_bound += 1
        low = lower_bound - 1
        high = lower_bound + 1
    
    ans = (high + low)/2
    while abs(base**ans - x) >= epsilon:
        if base**ans < x:
                low = ans
        else:
                high = ans
        ans = (high + low)/2
    print(ans, 'is close to the log base',base, 'of', x)
    return ans

x=30
epsilon= 0.5
base=8
y=log(x,base,epsilon)
print('y= ',y)
