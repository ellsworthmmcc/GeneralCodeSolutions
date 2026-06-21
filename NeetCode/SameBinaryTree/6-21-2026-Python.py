# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Recursive DFS
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Time Complexity:  O(n)
        # Space Complexity: O(n)

        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
    
    # Iterative BFS
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Time Complexity:  O(n)
        # Space Complexity: O(n)

        stackP = [p]
        stackQ = [q]

        while stackP or stackQ:
            if len(stackP) != len(stackQ):
                return False
            
            nodeP = stackP.pop()
            nodeQ = stackQ.pop()

            if nodeP is None and nodeQ is None:
                continue
            if nodeP is None or nodeQ is None:
                return False
            if nodeP.val != nodeQ.val:
                return False
            
            stackP.append(nodeP.left)
            stackP.append(nodeP.right)

            stackQ.append(nodeQ.left)
            stackQ.append(nodeQ.right)

        return True
