#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 19:18:43 2017

@author: christophernovitsky
"""

age = int(input("What is your current age? " ))
retire = int(input("What age would you like to retire? "))
years = retire - age 
time = 2017 + years
print(f"You have {years} years before you retire. It's 2017, so you can retire in {time}")