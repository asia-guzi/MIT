# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 20:01:54 2023

@author: Joanna.Guziwelakis
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 19:31:00 2023

@author: Joanna.Guziwelakis
"""
'''
x=int(input("wprowadź"))
epsilon = 0.01
num_guesses, low = 0, 0
high = max(1, x)
ans = (high + low)/2
while abs(ans**2 - x) >= epsilon:
    print('’low =‘', low, '‘high =‘', high, '‘ans =‘', ans)
    num_guesses += 1
    if ans**2 < x:
            low = ans
    else:
            high = ans
    ans =(high + low)/2
print('number o-F guesses =', num_guesses)
print(ans, 'is close to square root of', x)
'''
y=int(input("wprowadź"))
x=abs(y)
epsilon = 0.01
num_guesses, low = 0, 0
high = max(1, x)
ans = (high + low)/2
while abs(ans**2 - x) >= epsilon:
    print('’low =‘', low, '‘high =‘', high, '‘ans =‘', ans)
    num_guesses += 1
    if ans**2 < x:
            low = ans
    else:
            high = ans
    ans =(high + low)/2
    
if y>=0:
    print(ans, 'is close to square root of',x)  
else:
    print(-ans, 'is close to square root of',x)
    
print('number o-F guesses =', num_guesses)
