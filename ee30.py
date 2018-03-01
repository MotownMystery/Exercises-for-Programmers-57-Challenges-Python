#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 18:48:11 2017

@author: christophernovitsky
"""

import numpy as np 

X = np.arange(0,13)
M = np.zeros((13,13)) 

for i in range(0,13):
    M[i,:] = X*i
    print(M[i,:])
