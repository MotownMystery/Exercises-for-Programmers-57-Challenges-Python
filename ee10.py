#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 18:20:05 2017

@author: christophernovitsky
"""
num = input("Please input number of items? ")

Subtotal = 0
for i in range(1,int(num)+1):
    x = False
   
    while x == False:
        try: 
            price = float(input(f"Please enter the price of item {i}? "))
            quant = float(input(f"Please enter the quanity of item {i}?"))
            sub = price*quant
            x = True     
            Subtotal = Subtotal + sub 
        
        except ValueError:
            print("Enter a number > ")
            x = False 
tax = Subtotal*.055  
total = tax+Subtotal      
print(f"Subtotal: ${Subtotal}")
print(f"Tax: ${tax}")
print(f"Total: ${total}")

