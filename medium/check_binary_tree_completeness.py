from collections import deque

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        """Level order traversal using double-ended queue"""
        if root is None:
            return False

        q = deque()
        q.append(root)
        row_is_filled = True
        last_unfilled_node_count = 0

        while len(q) > 0:
            curr_node = q.popleft()
            if curr_node.left is None and curr_node.right is not None:
                return False  # right node isn't as far left as possible

            # enqueue children
            if curr_node.left is not None:
                q.append(curr_node.left)

            if curr_node.right is not None:
                q.append(curr_node.right)

            # see if the next node has children
            if not row_is_filled:
                if last_unfilled_node_count <= 1:
                    if curr_node.left is not None or curr_node.right is not None:
                        return False
                else:
                    if curr_node.left is None and curr_node.right is not None:
                        return False

            # see if we found an unfilled node that has children in the last level, and record how many children it had
            if row_is_filled and (curr_node.left is None or curr_node.right is None):
                if curr_node.left is not None:
                    last_unfilled_node_count += 1
                if curr_node.right is not None:
                    last_unfilled_node_count += 1
                row_is_filled = False

        return True
