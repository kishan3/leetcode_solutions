#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 11:16:06 2019

@author: kishan
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def bfsTraversal(self, root):
        queue = [root]
        result = []
        while queue:
            x = queue.pop(0)
            result.append(x.val)
            if x.left:    
                queue.append(x.left)
            if x.right:
                queue.append(x.right)
        return result
    def minValue(self, root):
        current=root
        while current.left:
            current=current.left
        return current
        
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return 
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                right = root.right
                root = None
                return right
            if not root.right:
                left = root.left
                root = None
                return left
            if root.left and root.right:
                minVal = self.minValue(root.right)
                root.val = minVal.val
                root.right = self.deleteNode(root.right, minVal.val)
        return root
    
s=Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.left.right = TreeNode(5)

s.deleteNode(root, 1)
s.bfsTraversal(root)
