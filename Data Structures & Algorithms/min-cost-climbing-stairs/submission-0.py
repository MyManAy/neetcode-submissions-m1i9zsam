class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        mapping = {}
        def rec(i):
            if i >= len(costs):
                return 0
            if i in mapping:
                return mapping[i]
            else:
                n = -1
                if i == -1:
                    n = 0
                else:
                    n = costs[i]
                val = min(n + rec(i+1), n + rec(i+2))
                mapping[i] = val
                return val

        return rec(-1)

        