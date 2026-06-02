# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Time Complexity:  O(n)
        # Space Complexity: O(n)
        maxDiameter = 0

        def getHeight(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            leftHeight = getHeight(node.left)
            rightHeight = getHeight(node.right)

            nonlocal maxDiameter
            maxDiameter = max(maxDiameter, leftHeight + rightHeight)

            return 1 + max(leftHeight, rightHeight)

        getHeight(root)
        return maxDiameter


# Iterative
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Time Complexity:  O(n)
        # Space Complexity: O(n)
        stack = [root]
        mp = {None: (0, 0)}

        while stack:
            node = stack[-1]

            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()

                leftHeight, leftDiameter = mp[node.left]
                rightHeight, rightDiameter = mp[node.right]

                mp[node] = (1 + max(leftHeight, rightHeight),
                            max(leftHeight + rightHeight, leftDiameter, rightDiameter))

        return mp[root][1]
