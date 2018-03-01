#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 19:52:57 2017

@author: christophernovitsky
"""
import math
X = False 
while X != True: 
    try:  
        people = float(input("How many people are you? "))
        pizza = float(input("How many pizza do you have? "))
        X = True 
    except ValueError:
        print('Non-numeric data found in the file. \n Please enter them in again?')
        X = False 
        
num = pizza*8
each = math.trunc(num/people) 
left = num%people 
print(f"{people} people and {pizza} pizzas")
print(f"Each person gets {each} pieces of pizza.")
print(f"There are {left} leftovers pieces")
