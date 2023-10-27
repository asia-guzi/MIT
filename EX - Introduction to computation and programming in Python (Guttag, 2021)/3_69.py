# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 14:25:27 2023

@author: Joanna.Guziwelakis
"""

# Finger exercise: Write a function is_in that accepts two strings as arguments and
# returns True if either string occurs anywhere in the other, and False otherwise.
# Hint: you might want to use the built-in str operator in.
# Finger exercise: Write a function to test is_in.
def is_in(str1,str2):
    if str2 in str1 or str1 in str2:
        
        return True
    else:
        return False





def test(is_in,str1,str2):
    if str2>str1:
        tempy2=str2
        str1=str2
        str2=tempy2
    x=None
    for index in range(len(str1)-len(str2)+1): #idea- sprawdzi ostatnie trzy, o potem już się nie zmieci cały drugi string
        if str1[index:index+len(str2)]==str2:
            x=True
        else:
            x=False
    print(x)  
    if x==is_in(str1,str2):
        return "is_in was right"
    
    else:
        return "is_in was not right"
    
        
        
str1=input("str1)")
str2=input("str2)")

print(is_in(str1,str2))
print(test(is_in,str1,str2))