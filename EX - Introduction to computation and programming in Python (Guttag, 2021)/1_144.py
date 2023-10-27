# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 19:46:27 2023

@author: Joanna.Guziwelakis
"""

'''


Finger exercise: Write a program that first stores the first ten numbers in the
Fibonnaci sequence to a file named fib_file. Each number should be on a sepa
rate line in the file. The program should then read the numbers from the file and
print them

'''
fibonaciii = open('fibonaci','w')
def fib(n):
    '''““Assumes n mt >= 0
    Returns Fibonacci of n”’”'''
   
    
    if n == 0 or n == 1:
        ans = 1
       
    else:
        ans = (fib(n-1) + fib(n-2))
    fibonaciii.write( str(n) + ',' + str(ans) + '\n''')
    
    return ans

n=20  #int(input('insert integer >0 n '))


print('f= ',fib(n))

# def test_f ib(n):
#     for i in range(n+1):
#         print(’fib of’, i, ‘=‘, fib(i))

fibonaciii.close()
fibonaciii = open('fibonaci', 'r')

#finisz = fibonaciii.readlines()

for line in fibonaciii:
    print(line)
    
# print(finisz)





