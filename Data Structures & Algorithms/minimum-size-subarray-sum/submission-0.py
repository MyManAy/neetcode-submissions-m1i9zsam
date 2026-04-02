class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        minLen = float('inf')
        runningSum = 0

        for i in range(len(nums)):
            runningSum += nums[i]
            while runningSum >= target:
                minLen = min(minLen, i - L + 1)
                runningSum -= nums[L]
                L += 1
            i += 1

        return 0 if minLen == float('inf') else minLen
        