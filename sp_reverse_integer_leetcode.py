#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 14:06:28 2019

@author: kishan
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign=1
        if x<0:
            sign=-1
        x=abs(x)
        import ipdb
        ipdb.set_trace()
        result = 0
        while x != 0:
            if abs(result) > 214748364:
                return 0
            result = (result * 10) + (x % 10)
            x = x//10
        return sign * result

s=Solution()
s.reverse(-123)