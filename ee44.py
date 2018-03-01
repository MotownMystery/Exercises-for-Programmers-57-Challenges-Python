#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 09:00:32 2017

@author: christophernovitsky
"""

Data = [{"name" : "widget", "price" : 2, "quantity" : 5}, 
        {"name" : "thing", "price" : 15, "quantity" : 5},
        {"name" : "doodad", "price" : 5, "quantity" : 10}]
X = [d["name"] for d in Data]

while True: 
    try:
        name = input("What is the name of the product? ").lower()
        break
    except ValueError:
        print("error")
        pass
    
id = X.index(name)
Price = Data[id]["price"]
Quantity = Data[id]["quantity"]

print("\n")
print("Name: ",name)
print("Price: ",Price)
print("Quantity: ",Quantity)