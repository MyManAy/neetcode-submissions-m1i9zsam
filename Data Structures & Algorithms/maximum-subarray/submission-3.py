class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = max(nums)
        currSum = 0
        for i in range(0, len(nums)):
            currSum += nums[i]
            if currSum < 0:
                currSum = 0
                continue
            if currSum > maxSum:
                maxSum = currSum
    
        return maxSum

        