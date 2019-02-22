#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 11:21:13 2018

@author: kishan
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        x = []
        for i in range(len(nums)):
            if nums[i] in x:
                return [i, nums.index(target - nums[i])]
            else:
                x.append(target - nums[i])


s = Solution()
s.twoSum([2, 7, 11, 19], 9)
