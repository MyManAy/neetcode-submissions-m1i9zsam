class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * len(prices) for _ in prices]

        for i in range(1, len(dp)):
            for j in range(len(dp) - i):
                profit = prices[j+i] - prices[j+i-1]
                if profit > 0:
                    dp[i][j] = dp[i-1][j] + profit
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[len(prices) - 1][0]

        