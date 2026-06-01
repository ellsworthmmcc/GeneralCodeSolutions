# Counter Solutions
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        return Counter(s) == Counter(t)
      
        
# Dict Solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        
        if len(s) != len(t):
            return False

        countDict: dict[str, int] = {}

        for char in s:
            countDict[char] = countDict.get(char, 0) + 1

        for char in t:
            if char not in countDict or countDict[char] == 0:
                return False
            countDict[char] -= 1

        return True
