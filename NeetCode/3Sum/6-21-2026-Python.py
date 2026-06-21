class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time Complexity:  O(n^2)
        # Space Complexity: O(1)
        # Sorting algorithm might use O(n) space complexity
        nums.sort()
        res = []

        for i in range(len(nums)):
            # if nums[i] is positive, all following values will also be positive
            # 3 positives can never equal 0
            if nums[i] > 0:
                break
            
            # Skip duplicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            while left < right:
                val = nums[i] + nums[left] + nums[right]
                
                if val > 0:
                    right -= 1
                elif val < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skips duplicate
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return res
