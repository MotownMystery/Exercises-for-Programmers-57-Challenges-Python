#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 21:05:18 2017

@author: christophernovitsky
"""

while True: 
    try: 
        a = float(input("What is the order amount? "))
        s = str(input("What is the state? "))
        break 
    except ValueError: 
        print("Enter a number >")
        
States = {'WI' : .055, 'MN' : .07}
tax = States[s]*a
print(tax)
print(tax+a)