class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time Complexity:  O(n)
        # Space Complexity: O(1)

        buyDay, sellDay = 0, 1
        profit = 0

        while sellDay < len(prices):
            if prices[buyDay] < prices[sellDay]:
                profit = max(profit, prices[sellDay] - prices[buyDay])
            else:
                buyDay = sellDay # found cheaper buy day
            sellDay += 1

        return profit
