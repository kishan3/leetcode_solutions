#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 12:17:53 2019

@author: kishan
"""


def get_range(from_, to):
    if from_ == to:
        return str(from_)
    return "{} -> {}".format(from_, to)


def find_missing_ranges(array, start, end):
    ranges = []
    prev = start - 1
    for i in range(len(array) + 1):
        if i == len(array):
            curr = end + 1
        else:
            curr = array[i]
        if curr - prev >= 2:
            ranges.append(get_range(prev + 1, curr - 1))
        prev = curr
    return ranges


find_missing_ranges([3, 4, 50, 750], 100, 999)
