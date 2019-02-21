#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 11:22:01 2018

@author: kishan
"""

class Solution(object):
    def bsearch(self, nums, key, start):
        left = start
        right = len(nums)-1
        while left<right:
            mid = (left+right)//2
            if nums[mid] < key:
                left=mid+1
            else:
                right=mid
        if left == right and nums[left] == key:
            return left
        return -1
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indexes=[]
        for i in range(len(nums)):
            key = target-nums[i]
            j = self.bsearch(nums, key, i+1)
            if j!=-1:
                indexes.append([i,j])
        return indexes

# Here try to decrease or increase pointers based on A[i]+A[j] value.
# Let’s assume we have two indices pointing to the ith and jth elements, 
# Ai and Aj respectively.
# The sum of Ai and Aj could only fall into one of these three possibilities:
# i. Ai + Aj > target. Increasing i isn’t going to help us, as it makes the 
# sum even bigger. Therefore we should decrement j.
# ii. Ai + Aj < target. Decreasing j isn’t going to help us, as it makes the sum even
# smaller. Therefore we should increment i.
# iii. Ai + Aj == target. We have found the answer      

class Solution2(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start=0
        end=len(nums)-1
        indexes=[]
        while start<end:
            total=nums[start]+nums[end]
            if total<target:
                start+=1
            elif total>target:
                end-=1
            else:
                indexes.append([start,end])
                start+=1
                end-=1
        return indexes
    
s=Solution2()
s.twoSum([1,2,4,6,10,12], 16)