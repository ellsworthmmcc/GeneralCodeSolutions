# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Time Complexity:  O(n)
        # Space Complexity: O(n)

        stack = []
        node = root
        lastNode = None
        depths = {}

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or lastNode == node.right:
                    stack.pop()
                    left = depths.get(node.left, 0)
                    right = depths.get(node.right, 0)

                    if abs(left- right) > 1:
                        return False

                    depths[node] = 1 + max(left, right)
                    lastNode = node
                    node = None
                else:
                    node = node.right
        return True
