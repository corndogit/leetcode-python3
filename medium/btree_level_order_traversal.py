from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: TreeNode) -> list[list[int]]:
    if root is None:
        return [[]]
    out = [[root.val]]
    q = deque()
    if root.left is not None:
        q.append(root.left)
    if root.right is not None:
        q.append(root.right)

    while len(q) > 0:
        out.append([node.val for node in q])
        new_q = deque()
        for node in q:
            if node.left is not None:
                new_q.append(node.left)
            if node.right is not None:
                new_q.append(node.right)
        q = new_q

    return out
