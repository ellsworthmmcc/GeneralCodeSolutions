class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Time Complexity:  O(n)
        # Space Complexity: O(m)
        # m is amount of unique characters in s
        
        count = {}
        longest = 0
        left = 0
        maxCount = 0

        for right in range(0, len(s), 1):
            char = s[right]
            count[char] = 1 + count.get(s[right], 0)
            maxCount = max(maxCount, count[s[right]])

            if (right - left + 1) - maxCount > k:
                count[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)
            
        return longest
