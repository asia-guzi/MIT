# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 12:49:28 2023

@author: Joanna.Guziwelakis
"""

'''
Finger exercise: Implement a function that meets the specification below. Use a
try-except block. Hint: before starting to code, you might want to type something
like 1 + ‘a• into the shell to see what kind of exception is raised.
def sum_digits(s):
“Assumes s is a string
Returns the sum of the decimal digits in s
For example, if s is ‘a2b3c’ it returns 5”””


'''

def sum_digits(s):
    '''Assumes s is a string
    Returns the sum of the decimal digits in s
    For example, if s is ‘a2b3c’ it returns 5'''
   
    suma=0
    znak=0
    for x in s:
        try:
         
         suma = suma + int(x)
            
        except ValueError:
            znak += 1
           
        
        except:
            print('w ciągu znalazł się niezidentyfikowany znak')
        
    print( znak, ' elementów ciągu nie jest cyfrą') 
    return suma    
            
s = input('wprowdż ciąg znaków składający się z cyfr i liter: ')  
  
print('suma cyfr zwartych w ciągu wynosi: ', sum_digits(s))          