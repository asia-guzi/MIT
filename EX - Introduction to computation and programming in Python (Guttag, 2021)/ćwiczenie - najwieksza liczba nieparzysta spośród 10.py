# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 16:16:45 2023

@author: Joanna.Guziwelakis
"""




x=int(input("Please, insert an integer: "))
c=1
s=(f"{x}")
while c<10:
    x=int(input("Please, insert an integer: "))
    s=s+(f"{x}")
    c=c+1
    print(s)
    
    
    
    
x=int(input("Please, insert an integer: "))
c=1
s=x
while c<10:
    c=c+1
    x=int(input("Please, insert an integer: "))
    if x%2!=0 and x>s:
     s=x 
    else:
     s=s
if s%2!=0:
    print(s)
else:
    print("no odd number was entered, it")