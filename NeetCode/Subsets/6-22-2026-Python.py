class Solution:
    # Iterative Backtracking
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Time Complexity:  O(n * 2^n)
        # Space Complexity: O(n)
        
        res = [[]]
        

        for num in nums:
            res += [subset + [num] for subset in res]
        
        return res

    # Recursive Backtracking
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Time Complexity:  O(n * 2^n)
        # Space Complexity: O(n)
        
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
