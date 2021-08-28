# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 15:33:13 2021

@author: bhavy
"""
#Problem - Search Insert Position

#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the #index where it would be if it were inserted in order.

#You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0 
        high = len(nums)-1
        
        while low <= high:
            mid = (low+high)//2
            guess = nums[mid]
            if guess == target:
                return mid
            if guess > target:
                high = mid - 1
            else:
                low = mid + 1
        return low
        