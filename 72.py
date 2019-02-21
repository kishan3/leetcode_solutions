#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 16:29:34 2019

@author: kishan
"""

def edit_distance_between_two_strings(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    
    if len1 == 0 or len2 == 0:
        return len1 + len2
    
    dist = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
    for i in range(len1+1):
        dist[i][0] = i
    for j in range(len2+1):
        dist[0][j] = j
    
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            up=dist[i-1][j]
            left= dist[i][j-1]
            up_left=dist[i-1][j-1]
            if str1[i-1] == str2[j-1]:
                dist[i][j] = min(left, up, up_left)
            else:
                dist[i][j] = min(left, up, up_left) + 1
                
    return dist[len1][len2]
    
edit_distance_between_two_strings("horse", "rose")
edit_distance_between_two_strings("intention", "execution")
    