#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 14:02:45 2018

@author: kishan
"""

def longest_substring_with_at_most_2_unique_chars(string):
    i=0
    j=-1
    maxLen=0
    for k in range(1,len(string)):
        if string[k] == string[k-1]:
            continue
        if j>=0 and string[j] != string[k]:
            maxLen = max(k-i, maxLen)
            i = j+1
        j=k-1
    return maxLen

longest_substring_with_at_most_2_unique_chars("abaacd")
longest_substring_with_at_most_2_unique_chars("aaa")
longest_substring_with_at_most_2_unique_chars("eceba")