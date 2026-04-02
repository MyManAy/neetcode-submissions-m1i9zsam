class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        R = 1

        if len(prices) == 1:
            return 0
        
        profit = 0
        while R < len(prices):
            p = prices[R] - prices[L]
            profit = max(profit, p)
            if p > 0:
                R += 1
            else:
                L = R
                R = L+1

        return profit
        