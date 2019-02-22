#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 17:02:23 2018

@author: kishan
"""


class Solution(object):
    def reverseHelper(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sl = list(s)
        self.reverseHelper(sl, 0, len(sl) - 1)
        start_of_index = 0
        k = 0
        while k <= len(sl):
            if k == len(sl) or sl[k] == ' ':
                self.reverseHelper(sl, start_of_index, k - 1)
                start_of_index = k + 1
            k += 1
        return ''.join(sl)


s = Solution()
s.reverseWords("sky is blue")
