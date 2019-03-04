# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            lheight = self.maxDepth(root.left)
            rheight = self.maxDepth(root.right)
            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1
