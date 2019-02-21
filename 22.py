#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 11:05:14 2019

@author: kishan
"""
ans=[]
def brackets(res, op, cl, N):
    print(res, op, cl)
    if op == N and cl == N:
        ans.append(res)
        return
    else:
        if op < N:
            brackets(res+"(", op+1 , cl, N)
        if cl < op:
            brackets(res+")", op, cl+1, N)
        
brackets("", 0,0,2)
ans