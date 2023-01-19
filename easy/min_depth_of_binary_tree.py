# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.right and root.left:
            # recursively, find if the left or right has a shorter depth, returning the shortest
            return min(self.minDepth(root.right), self.minDepth(root.left)) + 1
        if root.right:
            # navigate to the right node
            return self.minDepth(root.right) + 1
        else:
            # navigate to the left node
            return self.minDepth(root.left) + 1
