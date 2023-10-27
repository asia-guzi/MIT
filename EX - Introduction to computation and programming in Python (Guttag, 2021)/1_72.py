# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 15:35:26 2023

@author: Joanna.Guziwelakis
"""

# Finger exercise: Write a function mult that accepts either one or two ints as ar
# guments. If called with two arguments, the function prints the product of the two
# arguments. If called with one argument, it prints that argument.


def mult(x,y=None):
    if y!= None :
        return print(x*y)
    else:
        return print(x)
    
a=int(input("wstaw a"))
y=int(input("wstaw y"))

mult(a,y)

mult(a)
