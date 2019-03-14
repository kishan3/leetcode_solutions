# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def height(self, root):
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        lh = self.height(root.left)
        rh = self.height(root.right)

        if abs(lh - rh) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False
