#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 12:14:13 2019

@author: kishan
"""

class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None
        
class Solution(object):
    def merge2List(self, l1, l2):
        dummyHead=ListNode(0)
        p=dummyHead
        while l1!=None and l2!=None:
            if l1.val <= l2.val:
                p.next=l1
                l1=l1.next
            else:
                p.next=l2
                l2=l2.next
            p=p.next
        if l1:
            p.next=l1
        if l2:
            p.next=l2
        return dummyHead.next
    
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Divide and conqure
        end = len(lists) - 1
        while end > 0:
            begin=0
            while begin < end:
                lists[begin]=self.merge2List(lists[begin], lists[end])
                begin+=1
                end-=1
        return lists[0]
    
s=Solution()
l1=ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l2=ListNode(1)
l2.next=ListNode(70)
l2.next.next=ListNode(99)
l3=ListNode(4)
l3.next=ListNode(10)
l3.next.next=ListNode(15)
k_sort=s.mergeKLists([l1, l2, l3])
curr=k_sort
result=[]
while curr:
    result.append(curr.val)
    curr=curr.next
print(result)