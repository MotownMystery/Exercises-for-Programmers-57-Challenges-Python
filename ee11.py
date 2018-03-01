#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 18:54:56 2017

@author: christophernovitsky
"""
Count = {"USA" : 1.187,"Bitcoin" : .0001, "Pound": .88}
cur = str(input("This is a euro conversion program. Pick the currency: USA, BITcoin or Pound "))

euro = float(input("How may euro's are you exchanging? "))

convert = float(Count[cur])*euro
print(f"You have {convert} {cur}'s")