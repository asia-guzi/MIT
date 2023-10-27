# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 16:45:10 2023

@author: Joanna.Guziwelakis
"""

total_cost=float(input("indicate the cost of your dream house: "))
annual_salary=float(input("insert annual salary: "))
proc=float(input("insert the part of salary to be saved monthly (decimal): "))
portion_saved= proc*(annual_salary/12)
portion_down_payment = 0.25*total_cost
current_savings=0
r=float(0.04)
rm=float(r/12)
c=0

while current_savings < portion_down_payment:
    current_savings=current_savings+portion_saved+current_savings*rm
    c=c+1
    
print("you will will be saving for ",c," months untill you can afford your dream house")
