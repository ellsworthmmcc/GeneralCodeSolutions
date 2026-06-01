class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        seen: set[int] = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
