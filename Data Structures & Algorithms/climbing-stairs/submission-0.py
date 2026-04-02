class Solution:
    dp = [1, 2]
    def climbStairs(self, n: int) -> int:
        if n > len(self.dp):
            return self.climbStairs(n-1) + self.climbStairs(n-2)
        else:
            return self.dp[n-1]

