class Solution:
    def isValid(self, s: str) -> bool:
        # Time Complexity:  O(n)
        # Space Complexity: O(n)

        # String can't be valid, unequal amount of parentheses
        if len(s) % 2 != 0:
            return False
        
        # Dict to hold corresponding open and closed parentheses
        opening: dict[str, str] = {
            '(' : ')',
            '{' : '}',
            '[' : ']',
        }
        
        stack = []

        for char in s:
            if char in opening:
                stack.append(char)
            else:
                if not stack or opening[stack.pop()] != char:
                    return False
                
        return len(stack) == 0
