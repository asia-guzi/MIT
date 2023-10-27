# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 10:06:29 2023

@author: Joanna.Guziwelakis
"""
"""
Finger exercise: Write a program that prints the sum of the prime numbers
greater than 2 and less than 1000. Hint: you probably want to have a ioop that is a
primality test nested inside a ioop that iterates over the odd integers between 3
and 999.
"""
c=0
suma=0
prime=0
odd=0
for prime in range(3,999,2):
   
    
   
    
   
    for odd in range(3,999,2):
        if odd<prime and prime%odd==0  :
            c=0 #jak to zamienić na true or false, bo raczej by było ładniej informatycznie - na booleen jak przemienić
            break
        elif odd<prime and prime%odd!=0:
            c=1
        else:  
            break
    
        
                
    if c==0:
            suma=suma
    else:
            suma=suma+prime
            print(prime)
"""
        
        
        while prime%odd==0:
           # break nie moze byc breaj bo wyjdzie z petli i nie bedzie dalej testował pierwszych
           check=1
        else:
            check=0
        if check==1:
           suma=suma+prime
        else:
            suma=suma
            
print(suma)        
         
        elif prime%odd!=0: 
           # prime%odd!=0:
            suma=suma+prime
            print(prime)
            print(suma)
            break
"""
print(suma)
