# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 16:06:25 2023

@author: Joanna.Guziwelakis
"""

'''

Finger exercise: Implement a function that meets the specification
117
def get_min(d)
\'''d a dict mapping letters to ints
returns the value in ci with the key that occurs first itt the
alphabet. E.g., if ci = {x = 11, b = 12}, get_mm returns 12.\'''


'''

import string

def get_min(d):
    '''d a dict mapping letters to ints
    returns the value in d with the key that occurs first in the
    alphabet. E.g., if d = {x = 11, b = 12}, get_mm returns 12.'''
    
    k=list(d.keys())
    mini=min(k)
    print(mini)
    ans=d[mini]
    print('ans=',ans)
    
    
    return  ans
    


d={}
z=string.ascii_lowercase
alfa = lambda x: -32*2+(z.index(x))**2
for i in range(0,len(z),len(z)//3):      
    x=string.ascii_lowercase[i]
    if  x in ['a','o', 'i', 'e', 'u']:
     d[x]=alfa(x)   
    else:
     d[x]=-alfa(x)


dl=list(d.items())
wl=list(d.items())
print('dl=',dl)     
strv=d.values()
kol=sorted(strv)
print('kol=',kol)
c=0
for i in strv:
    print('i=',i)
    print('c=',c)
    msc=kol.index(i)
    ('msc=',msc)
    wl.remove(wl[msc])
    wl.insert(msc,dl[c])
    
    print('wl=',wl)
    
    c=c+1

d=dict(wl)
print('d=',d)



print('ans=',get_min(d))
        
print('items d=', d.items() ) 