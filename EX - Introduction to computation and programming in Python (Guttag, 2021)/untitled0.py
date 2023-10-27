# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 14:51:06 2023

@author: Joanna.Guziwelakis
"""

total_cost = float(input('put total cost of your dream house:'))
annual_salary = float(input('what is your annual salary?:'))
portion_saved = float(input('portion of your salary witch you want to be saved?:'))
portion_down_payment = 0.25
r = 0.04
c = 0
current_savings = 0.0
while current_savings <= total_cost*portion_down_payment:
    current_savings = portion_saved*annual_salary
    currant_savings = (current_savings*r)/12
    c+=1
print('num of months', c)