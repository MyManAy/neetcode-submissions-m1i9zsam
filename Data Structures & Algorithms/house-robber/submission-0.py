class Solution:
    def rob(self, nums: List[int]) -> int:
        mapping = {}
        def robrec(i):
            if i in mapping:
                return mapping[i]
            elif i == 0:
                mapping[i] = nums[i]
                return mapping[i]
            elif i == 1:
                mapping[i] = max(nums[i], nums[i - 1])
                return mapping[i]
            else:
                mapping[i] = max(nums[i] + robrec(i - 2), robrec(i - 1))
                return mapping[i]

        return robrec(len(nums)-1)

        