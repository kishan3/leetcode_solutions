#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 14:52:33 2018

@author: kishan
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not needle and not haystack:
            return -1
        if len(needle) > len(haystack):
            return -1
        window=len(needle)
        i=0
        while i<len(haystack):
            current_window=haystack[i:i+window]
            if current_window==needle:
                return i
            i+=1
        return -1

s=Solution()
s.strStr("aaaab", "aa")