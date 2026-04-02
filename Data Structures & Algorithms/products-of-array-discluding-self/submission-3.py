class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        toReturn = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            toReturn[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            toReturn[i] *= suffix
            suffix *= nums[i]

        return toReturn
            