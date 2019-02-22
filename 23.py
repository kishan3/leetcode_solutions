#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 14:40:09 2018

@author: kishan
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = []
        if not l1:
            return l2

        head1 = l1[0]
        head2 = l2[0]
        while True:

            if not head1 or not head2:
                break
            if head1.val < head2.val:
                result.append(head1)
                head1 = head1.next
            else:
                result.append(head2)
                head2 = head2.next
        if head1:
            while head1:
                result.append(head1)
                head1 = head1.next
        if head2:
            while head2:
                result.append(head2)
                head2 = head2.next
        return result

    def mergeKlists(self, lists):
        merged_list = []
        for i in lists:
            merged_list.extend(self.mergeTwoLists(merged_list, i))
            print(merged_list)
        return [i.val for i in merged_list]


l1 = ListNode(2)
l1.next = ListNode(1)
l1.next.next = ListNode(4)

l2 = ListNode(20)
l2.next = ListNode(30)
l2.next.next = ListNode(80)
l4 = ListNode(5)
l4.next = ListNode(10)
l4.next.next = ListNode(15)
l3 = [[l1], [l2], [l4]]
s = Solution()
print(s.mergeKlists(l3))
