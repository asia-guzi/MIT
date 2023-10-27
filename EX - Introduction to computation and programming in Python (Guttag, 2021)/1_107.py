# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 12:31:05 2023

@author: Joanna.Guziwelakis
"""

'''
Finger exercise: Implement a function satisfying the following specification.
I-lint: it will be convenient to use lambda in the body of the implementation.
def f(Li, L2):
“““Li, L2 lists of same length of numbers
returns the sum of raising each element in Li
to the power of the element at the same index in L2
For example, f([l,2], [2,3]) returns 9’”

'''



# def f(L1, L2):
#     '''L1, L2 lists of same length of numbers
#     returns the sum of raising each element in L1
#     to the power of the element at the same index in L2
#     For example, f([l,2], [2,3]) returns 9'''
    
#     pot=[]
#     for i in range(len(L1)):
    
#     pot.appened(lambda L1[i]**L2[i])
    
#     return pot

def f(L1, L2):
    '''L1, L2 lists of same length of numbers
    returns the sum of raising each element in L1
    to the power of the element at the same index in L2
    For example, f([l,2], [2,3]) returns 9'''
    
    pot=list()
    
    for i in range(len(L1)):
        x=lambda L1, L2, pot :  pot.append(L1**L2)  
        x(L1[i], L2[i], pot)
    return pot

def f(L1, L2):
    '''L1, L2 lists of same length of numbers
    returns the sum of raising each element in L1
    to the power of the element at the same index in L2
    For example, f([l,2], [2,3]) returns 9'''
    
    pot=list()
    x=lambda L1, L2, pot :  pot.append(L1**L2) 
    
    for i in range(len(L1)):
         
        x(L1[i], L2[i], pot)
    return pot

'''nie'''      
# def f(L1, L2):
#     '''L1, L2 lists of same length of numbers
#     returns the sum of raising each element in L1
#     to the power of the element at the same index in L2
#     For example, f([l,2], [2,3]) returns 9'''
    
#     pot=[]
#     for i in range(len(L1)):
#         lambda L1[i] , L2[i] : L1[i]**L2[i]
#         pot.appened(x)
#     return pot

'''nie'''  
# def f(L1, L2): 
#     '''L1, L2 lists of same length of numbers
#     returns the sum of raising each element in L1
#     to the power of the element at the same index in L2
#     For example, f([l,2], [2,3]) returns 9'''
    
#     pot=[]
#     for i in lambda L1[i] , L2[i] : L1[i]**L2[i]:
#         pot.appened(i)
#     return pot


# def f(L1, L2):
#     '''L1, L2 lists of same length of numbers
#     returns the sum of raising each element in L1
#     to the power of the element at the same index in L2
#     For example, f([l,2], [2,3]) returns 9'''
#     lambda x, y : x**y
#     pot=[]
#     la=lambda x,y : x**y
#     for i in range(len(L1)):
#         pot.append(la(L1[i], L2[i]))
    # return pot

def f(L1, L2):
    '''L1, L2 lists of same length of numbers
    returns the sum of raising each element in L1
    to the power of the element at the same index in L2
    For example, f([l,2], [2,3]) returns 9'''
    lambda x, y : x**y
    pot=[]
    la=lambda x,y : x**y
    for i in range(len(L1)):
        pot.append(la(L1[i], L2[i]))
    return pot

L1=[2,3,4,5,6,7,8,9]
L2=[3,2,1,3,2,1,2,1]

pot=f(L1, L2)
print(pot)
print('suma=',sum(pot))
    
