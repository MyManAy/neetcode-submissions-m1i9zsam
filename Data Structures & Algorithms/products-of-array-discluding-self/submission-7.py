class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            saved = nums[i]
            res[i] *= prefix
            prefix *= saved

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            saved = nums[i]
            res[i] *= suffix
            suffix *= saved

        return res

        