# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 23:55:10 2020

@author: ARCHISMAN ROY
"""

s_list = [21,32,14,29,43]
print(s_list)
key = input("Enter the key element you want to search for :")
k=int(key)
a = s_list.index(k)
print("It is at index",a)