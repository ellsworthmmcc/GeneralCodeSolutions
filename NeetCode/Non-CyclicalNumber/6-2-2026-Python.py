class Solution:
    def sumOfSquares(self, n:int) -> int:
        # Time Complexity:  O(log n)
        # Space Complexity: O(1)

        res = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            res += digit
            n = n // 10

        return res

    def isHappy(self, n: int) -> bool:
        # Time Complexity:  O(log n)
        # Space Complexity: O(1)
        slow = n
        fast = self.sumOfSquares(n)

        while fast != 1 and slow != fast:
            slow = self.sumOfSquares(slow)
            fast = self.sumOfSquares(self.sumOfSquares(fast))

        return fast == 1
