class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mapping = {}
        def rec(r, c):
            if ((r, c) in mapping):
                return mapping[(r, c)]
            if min(r, c) <= 0:
                return 0
            elif ((r, c) == (1, 1)):
                return 1
            else:
                mapping[(r, c)] = rec(r-1, c) + rec(r, c-1)
                return mapping[(r, c)]
        return rec(m, n)
        