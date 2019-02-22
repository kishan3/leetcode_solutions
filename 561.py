#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 09:33:07 2018

@author: kishan
"""


def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False
    s1map = [0] * 26
    for i in s1:
        s1map[ord(i) - ord('a')] += 1
    print('S1MAP: ', s1map)
    i = 0
    while i <= len(s2) - len(s1):
        s2map = [0] * 26
        for j in range(len(s1)):
            s2map[ord(s2[i + j]) - ord('a')] += 1
        print('S2MAP: ', s2map)
        if s1map == s2map:
            return True
        i += 1
    return False


checkInclusion("ab", "eidbaooo")
checkInclusion("ab", "eidoo")
checkInclusion("ab", "ba")


# Instead of generating the hashmap afresh for every window considered in s2,
# we can create the hashmap just once for the first window in s2s2. 
# Then, later on when we slide the window, we know that we add one preceding 
# character and add a new succeeding character to the new window considered. 
# Thus, we can update the hashmap by just updating the indices associated with 
# those two characters only. Again, for every updated hashmap, we compare all 
# the elements of the hashmap for equality to get the required result.

def checkInclusion2(s1, s2):
    if len(s1) > len(s2):
        return False
    s1map = [0] * 26
    s2map = [0] * 26
    for i in range(len(s1)):
        s1map[ord(s1[i]) - ord('a')] += 1
        s2map[ord(s2[i]) - ord('a')] += 1
    for i in range(len(s2) - len(s1)):
        if s1map == s2map:
            return True
        s2map[ord(s2[i + len(s1)]) - ord('a')] += 1
        s2map[ord(s2[i]) - ord('a')] -= 1
    return s1map == s2map


checkInclusion2('ab', 'ediobaooo')
checkInclusion2('adc', 'dcda')
checkInclusion2('adc', 'dcda')
