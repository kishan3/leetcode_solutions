#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 15:09:06 2019

@author: kishan
"""
def permuteStringHelper(string, chosen, answers):
    if not string:
        print(chosen)
        answers.append(chosen)
    else:
        for i in range(len(string)):
            ch = string[i]
            chosen += ch
            index = string.index(ch)
            string = string[:index] + string[index+1:]
            
            permuteStringHelper(string, chosen, answers)
            string = string[:index] + ch + string[index:]
            chosen = chosen[:-1]
            
def permuteString(string):
    answers = []
    permuteStringHelper(string, "", answers)
    return answers
len(permuteString("kishan"))