# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 17:57:41 2023

@author: Joanna.Guziwelakis
"""

'''
Finger exercise: Write a lambda expression that has two numeric parameters. If
the second argument equals zero, it should return None. Otherwise it should re
turn the value of dividing the first argument by the second argument. Hint: use a
conditional expression
'''

div=lambda x, y: None if y==0 else x/y

print(div(10,0))