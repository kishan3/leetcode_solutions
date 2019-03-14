# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def helper(self, root, start, end):
        if start > end:
            return
        mid = (start + end) // 2
        node = TreeNode(root[mid])
        node.left = self.helper(root, start, mid - 1)
        node.right = self.helper(root, mid + 1, end)
        return node

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.helper(nums, 0, len(nums) - 1)
