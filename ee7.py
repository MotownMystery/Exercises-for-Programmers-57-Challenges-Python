#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 19:38:21 2017

@author: christophernovitsky
"""
x, y = '', ''
while x != x.isnumeric or y != y.isnumeric:
    
    x = input("What is the length of the room? ")
    y = input("What is the width of the room? ")
    
I_area = int(x)*int(y)
M_area = I_area*.09290304
print(f"The dimensions of the room are {x} feet by {y} feet")
print(f" The area is \n {I_area} square feet \n {M_area} square meters")

