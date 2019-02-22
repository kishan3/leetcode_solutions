#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 14:51:40 2019

@author: kishan
"""


def is_one_edit_distance(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    if len1 > len2:
        return is_one_edit_distance(str2, str1)
    if (len2 - len1) > 1:
        return False

    i = 0
    j = 0
    difference_count = 0
    while i < len1 and j < len2:
        if str1[i] == str2[j]:
            i += 1
            j += 1
        else:
            if difference_count >= 1:
                return False
            if len1 == len2:
                i += 1
                j += 1
            else:
                i += 1

            difference_count += 1
    if i < len1 or j < len2:
        difference_count += 1
    return difference_count == 1


is_one_edit_distance("abcxes", "abcde")
