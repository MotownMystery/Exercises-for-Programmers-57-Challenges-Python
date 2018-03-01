#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 23:35:46 2017

@author: christophernovitsky
"""
import math as m 

def Num_Payoff(b,i,p):
    n = (-1/30)*m.log(1+(b/p)*(1-(1+i**30)),10)/m.log(1+i,10)
    return n 

b = int(input("What is your balance? "))
i = float(input("What is your APR? "))/100
p = int(input("What is your monthly payment? "))

print(Num_Payoff(b,i,p))

#print(f"It will take you {} months to pay off this card")
