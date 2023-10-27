# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 17:41:20 2023

@author: Joanna.Guziwelakis
"""
"""

#Newton-Raphson for square root
# Find x such that x**2 - 24 is within epsilon of 0
k=int(input('wpisz liczbę'))
epsilon=0.01
guess = k/2
while abs(guess**2 - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
print('Square root of’', k, 'is about', guess)


Finger exercise: Add some code to the implementation of Newton—Raphson that
keeps track of the number of iterations used to find the root. Use that code as
part of a program that compares the efficiency of Newton-Raphson and bisec
tion search. (You should discover that Newton—Raphson is far more efficient.)

"""

#bisection search
epsilon=0.01
bs=0
nr=0
k=int(input('wpisz liczbę'))
high=abs(k)
low=0
guess=0

while  abs(k-guess**2)>=epsilon:
    bs=bs+1
    guess=(low+high)/2
    if (k-guess**2)>epsilon:
        low=guess
    elif (k-guess**2)<= -epsilon:
        high=guess
print('Square root of’', k, 'is about', guess)       
print(bs) 
 
guess = k/2
while abs(guess**2 - k) >= epsilon:
     guess = guess - (((guess**2) - k)/(2*guess))
     nr=nr+1
print('Square root of’', k, 'is about', guess)  
print(nr)     