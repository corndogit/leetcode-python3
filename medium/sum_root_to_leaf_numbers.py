class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        root_to_leaf_nums = []

        def traverseToFindNum(node, stack=None):
            if stack is None:
                stack = []
            stack.append(node.val)
            if node.left is None and node.right is None:
                root_to_leaf_nums.append(int("".join(str(s) for s in stack)))
                return

            if node.left:
                traverseToFindNum(node.left, stack.copy())

            if node.right:
                traverseToFindNum(node.right, stack.copy())

        traverseToFindNum(root)

        return sum(root_to_leaf_nums)


if __name__ == '__main__':
    sol = Solution()
    tree = TreeNode(1, TreeNode(2), TreeNode(3))
    print(sol.sumNumbers(tree))
