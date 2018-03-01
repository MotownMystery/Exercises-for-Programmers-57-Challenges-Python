#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 18:47:34 2017

@author: christophernovitsky
"""

x = str(input("What is the input string? "))

while x== "":
    print("Please enter your name")
    x = str(input("What is the input string? "))


print(f"{x} has {len(x)} characters")

