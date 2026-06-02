# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Time Complexity:  O(n)
        # Space Complexity: O(n)
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Iterative
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Time Complexity:  O(n)
        # Space Complexity: O(n)
        if not root:
            return 0

        queue = deque([root])
        depth = 0

        while queue:
            # Processes all nodes at current level
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            depth += 1
        
        return depth
