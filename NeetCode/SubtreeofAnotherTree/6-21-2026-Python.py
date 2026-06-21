# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Srting Serialization
class Solution:   
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        stack = [root]

        treeStr = ''

        while stack:
            node = stack.pop()
            if node is None:
                treeStr += '$#'
                continue
            else:
                treeStr += f'${node.val}'
                stack.append(node.right)
                stack.append(node.left)
        
        return treeStr
    

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Time Complexity: O(n * m)
        # Space Complexity: O(n + m)
        # n = num of nodes in root tree, m = num of nodes in sub tree

        rootStr = self.serialize(root)
        subStr = self.serialize(subRoot)

        return subStr in rootStr
