class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time Complexity:  O(log(n))
        # Space Complexity: O(1)

        left, right = 0, len(nums) - 1
        
        while left <= right:
            # Helps to avoid integer overflow, 
            # doesn't create a value larger than any that already exist
            pivot = left + (right - left) // 2
            value = nums[pivot]
            if value == target:
                return pivot
            
            if value < target:
                left = pivot + 1
            else:
                right = pivot - 1

        return -1
