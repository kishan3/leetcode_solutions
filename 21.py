#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 14:08:44 2018

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
        head1 = l1
        head2 = l2

        while True:

            if not head1 or not head2:
                break
            if head1.val < head2.val:
                result.append(head1.val)
                head1 = head1.next
            else:
                result.append(head2.val)
                head2 = head2.next
        while head1:
            result.append(head1.val)
            head1 = head1.next
        while head2:
            result.append(head2.val)
            head2 = head2.next
        return result


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(20)
l2.next = ListNode(30)
l2.next.next = ListNode(80)
s = Solution()
print(s.mergeTwoLists(l1, l2))
