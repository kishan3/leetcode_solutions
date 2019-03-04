# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        current = root
        stack = []
        result = []
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                if len(stack) > 0:
                    x = stack.pop()
                    result.append(x.val)
                    current = x.right
                else:
                    break
        return result
