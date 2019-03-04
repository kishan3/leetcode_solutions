# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # def isBSTHelper(self, root, mini, maxi):
    #     if not root:
    #         return True
    #     if root.val <= mini or root.val >= maxi:
    #         return False
    #     return (self.isBSTHelper(root.left, mini, root.val) and
    #             self.isBSTHelper(root.right, root.val, maxi))
    # def isValidBST(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     INT_MAX = float('inf')
    #     INT_MIN = float('-inf')
    #     return self.isBSTHelper(root, INT_MIN, INT_MAX)

    def isValidBST(self, root):
        if not root:
            return True
        stack = [(root, None, None)]

        while stack:
            root, lo, up = stack.pop()
            if root.right:
                if root.right.val > root.val:
                    if up and root.right.val >= up:
                        return False
                    stack.append((root.right, root.val, up))
                else:
                    return False
            if root.left:
                if root.left.val < root.val:
                    if lo and root.left.val <= lo:
                        return False
                    stack.append((root.left, lo, root.val))
                else:
                    return False
        return True
