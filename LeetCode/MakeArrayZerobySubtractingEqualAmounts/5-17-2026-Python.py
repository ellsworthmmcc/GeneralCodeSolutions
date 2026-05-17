class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        # Time Complexity:  O(n)
        # Space Complexity: O(k)
        # k is number of distinct values
        
        # Number of operations is equal to the number of distinct non-zero values
        return len(set(nums) - {0})
