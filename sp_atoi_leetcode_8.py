#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 10:12:50 2018

@author: kishan
"""

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str)==0:
            return 0
        INT_MAX=(2**31)-1
        INT_MIN=-2**31
        sign=1
        i=0
        while i<len(str) and str[i]==' ':
            i+=1
        if i<len(str) and str[i] == '+':
            i+=1
        elif i<len(str) and str[i] == '-':
            sign = -1
            i+=1
        num=0
        while i<len(str) and str[i].isdigit():
            digit=int(str[i])
            num=num*10+digit
            if sign*num >= INT_MAX:
                return INT_MAX
            if sign*num <= INT_MIN:
                return INT_MIN
            i+=1
        return sign*num

s=Solution()
s.myAtoi("    +42")
s.myAtoi("    -42")