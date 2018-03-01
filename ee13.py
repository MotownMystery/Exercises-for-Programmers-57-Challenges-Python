#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 20:42:54 2017

@author: christophernovitsky
"""

from babel.numbers import format_currency


while True:
    try: 
        P = float(input("Enter principle? "))
        r = float(input("Enter the intrest rate? "))
        t = int(input("Enter the number of years? " ))
        n = float(input("Number of time a year intrest compound? "))
        break
    except ValueError:
        print("Enter a number")
        
for i in range(1,t+1):
    A = P*(1+((r/100)/n))**(n*float(i))
    print("Year " + str(i) + ": " + format_currency(A, 'USD', locale='en_US'))
    


