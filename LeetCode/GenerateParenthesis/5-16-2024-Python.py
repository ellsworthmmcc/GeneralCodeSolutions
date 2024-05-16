class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # Time Complexity:  O(2^n)
        # Space Complexity: O(2^n)

        # Holds parenthesis to be returned at function end
        parenthesis = []

        # Left represents left parenthesis in current gen and right likewise
        left = right = 0

        # Holds the left, right, and paren to allow an iterative solution
        parenthesisGenerator = [(left, right, '')]

        # Loops until all possible permutations have been found
        # Only adds ')' after valid '('
        while parenthesisGenerator:

            # Retrieves what previous iteration generated
            left, right, paren = parenthesisGenerator.pop()

            # Means current parenthesis grouping as been found
            if left==right and left+right == n * 2:
                parenthesis.append(paren)

            # Maximum amount of left/right parenthesis is equal to n
            if left < n:
                parenthesisGenerator.append((left + 1, right, paren + '('))
            if right < left:
                parenthesisGenerator.append((left, right + 1, paren + ')'))
        
        return parenthesis
