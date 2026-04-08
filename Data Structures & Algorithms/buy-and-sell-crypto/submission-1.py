class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = 0
        l = 0
        r = 1

        if len(prices) <= 1:
            return 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r = r + 1
                continue

            maxPrice = max(maxPrice, prices[r] - prices[l])
            r += 1

        return maxPrice

        