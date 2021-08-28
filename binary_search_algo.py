# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 14:08:42 2021

@author: bhavy
"""
def binary_search(list,item):
    low = 0
    high = len(list)-1
    
    while low<=high:
        mid = (low+high)//2 #I have used '//' indicates floor division in python 3.x. 
        #If we use '/' the resulting mid  is a float which is not allowed for list indicies
        guess = list[mid]
        if guess == item:
            return mid
        if guess>item:
            high = mid-1
        else:
            low = mid+1
    return None

my_list = [1,3,5,7,9,11]

print(binary_search(my_list, -1))
    