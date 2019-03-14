# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # DFS

        # BFS
        if not root:
            return 0
        queue = [(1, root)]
        while queue:
            depth, root = queue.pop(0)
            if not root.left and not root.right:
                return depth
            for child in [root.left, root.right]:
                if child:
                    queue.append((depth + 1, child))
