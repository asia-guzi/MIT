# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 14:25:27 2023

@author: Joanna.Guziwelakis
"""

# Finger exercise: Write a function is_in that accepts two strings as arguments and
# returns True if either string occurs anywhere in the other, and False otherwise.
# Hint: you might want to use the built-in str operator in.

def is_in(str1,str2):
    if str2 in str1 or str1 in str2:
        
        return True
    else:
        return False
    
str1=input("str1)")
str2=input("str2)")
print(is_in(str1,str2))