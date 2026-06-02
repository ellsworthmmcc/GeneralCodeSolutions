# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Time Complexity:  O(n)
        # Space Complexity: O(n)
        if not root:
            return None
        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        
        return root

# Iterative
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Time Complexity:  O(n)
        # Space Complexity: O(n)
        if not root:
            return None

        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        
        return root
