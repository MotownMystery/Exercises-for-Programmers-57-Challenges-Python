#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 20:20:13 2017

@author: christophernovitsky
"""

while True:
    try: 
        P = float(input("Enter principle? "))
        r = float(input("Enter the intrest rate? "))
        t = int(input("Enter the number of years? " ))
        break
    except ValueError:
        print("Enter a number")
    

for i in range(1, t+1):
    A = P*(1+(r/100)*i)
    print("After " + str(i) + " years " + str(round(A)))
    