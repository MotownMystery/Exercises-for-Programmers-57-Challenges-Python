#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 21:23:18 2017

@author: christophernovitsky
"""
while True: 
    try:
        a = int(input('What is your age? '))
        break
    except ValueError:
        print('error')
        
if a > 17 and a > 0: print("You can drive!")
if a < 18: print("You can't drive...")

