class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = float('-inf')
        L = 0
        runningMap = set()
        for R in range(len(s)):
            while s[R] in runningMap:
                runningMap.remove(s[L]) 
                L += 1
            maxLen = max(maxLen, R - L + 1)
            runningMap.add(s[R])
        
        return 0 if maxLen == float('-inf') else maxLen