# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 20:06:09 2023

@author: Joanna.Guziwelakis
"""
'''
Finger exercise: The Empire State Building is 102 stories high. A man wanted to
know the highest floor from which he could drop an egg without the egg break
ing. He proposed to drop an egg from the top floor. If it broke, he would go down
a floor, and try it again. He would do this until the egg did not break. At worst,
this method requires 102 eggs. Implement a method that at worst uses seven eggs.
'''
high=max(1,102)
low=1
guess=int((high+low)/2)
c=0
b=0

#1 nie zbiło się, 0 zbiło się
" reprezenruje rozbicie jaja = 1 nie rozbiło się, b>1 nie rozbiło sie i mozna zobaczyc czy wyzej tez sie nie rozbije b<1 rozbiło sie itrzeba zerknąć czy sie rozbije dalej"
while b==0 and high!=guess:
    c=c+1
   
    if b==1:
        break
    elif b==0:
        print('high=',high)
        print('guess=',guess)
        
        high=guess
    else:
        break
    guess=int((high+low)/2)
    
        
print(c)    
if b==1:
     print('można zrzucić z ',guess,'piętra')
     
else:
    print('niemożna zrzucić wcale ')