class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time Complexity:  O(n)
        # Space Complexity: O(n)

        # Maps number to its corresponding index
        seen: dict[int, int] = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        
        # Return empty list if target not found
        return []
