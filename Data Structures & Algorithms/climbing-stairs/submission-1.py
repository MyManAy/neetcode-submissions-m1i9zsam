class Solution:
    def climbStairs(self, n: int) -> int:
        sols = {1: 1, 2: 2}
        def rec(n):
            if n in sols:
                return sols[n]
            else:
                sol = rec(n-1) + rec(n-2)
                sols[n] = sol
                return sol
            
        return rec(n)

        