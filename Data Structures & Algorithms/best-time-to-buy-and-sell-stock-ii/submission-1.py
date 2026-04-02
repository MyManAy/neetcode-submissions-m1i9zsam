class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[i-1]
            prev = prev + profit if profit > 0 else prev

        return prev 

        