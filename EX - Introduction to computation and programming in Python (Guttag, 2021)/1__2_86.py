# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 18:05:15 2023

@author: Joanna.Guziwelakis
"""

'''
Finger exercise: What does s.find(sub) return if sub does not occur in s?
Finger exercise: Use find to implement a function satisfying the specification

 def find_last(s, sub):
\'''s and sub are non-empty strings
Returns the index of the last occurrence of sub in s.
Returns None if sub does not occur in s\'''   
    
'''

# # f1
# s='ksjdlehdkhlksd'
# print(s.find('leh'))

def find_last(s, sub):

    '''s and sub are non-empty strings
    Returns the index of the last occurrence of sub in s.
    Returns None if sub does not occur in s'''
    if sub in s:
        return s.find(sub)
    
        
    return None
    
    
    
    
s=input('wstraw string: ')
sub=input('wstaw sub: ')
print(find_last(s, sub))

