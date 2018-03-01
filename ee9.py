#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 22:27:48 2017

@author: christophernovitsky
"""
import math 

room = input("Is the room round or rec? " )

if room == 'rec':
    x = False 
    while x == False:
        try: 
            l = float(input("Lenght of roof? "))
            w = float(input("Width of roof? "))
            x = True
        except ValueError:
            print("Enter a number > ")
            x = False 
            

    area = l*w
    paint = math.ceil(area/360)
    print(f"You will need to purchase {paint}\n gallons of paint to cover {area} squre feet")
  
    
if room == 'round':
    x = False 
    while x == False:
        try: 
            r = float(input("Radius of roof? "))
            x = True
        except ValueError:
            print("Enter a number > ")
            x = False 
    area = math.pi*r**2
    paint = math.ceil(area/360) 
    print(f"You will need to purchase {paint}\n gallons of paint to cover {area} squre feet")