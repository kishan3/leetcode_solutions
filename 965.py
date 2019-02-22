#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 19:27:57 2018

@author: kishan
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if (root.left and root.val != root.left.val) or (root.right and root.val != root.right.val):
            return False
        if root.left:
            return self.isUnivalTree(root.left)
        if root.right:
            return self.isUnivalTree(root.right)
        return True
