class Solution:
    def hammingWeight(self, n: int) -> int:
        # Time Complexity:  O(k)
        # Space Complexity: O(1)
        # k is the amount of bits
        bits = 0

        while n:
            n &= n - 1
            bits += 1

        return bits
