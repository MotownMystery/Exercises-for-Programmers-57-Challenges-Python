#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 23:58:35 2017

@author: christophernovitsky
"""

def isAnagram(str1,str2):   
    
    if len(str1) != len(str2):
        print("Is not an Anagram")
    
    else: 
        x = 0 
        for i in range(0, len(str2)):
            index = str1.find(str2[i])
            
            if  i == (len(str2)-1):
                print('It is an Anagram') 
                return
            if index == -1: 
                print("Not an Anagram")
                return 
            else: 
                x +=x
                 
                
isAnagram('note','tone')

        
        
    
    
        