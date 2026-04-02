class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(1, len(nums)):
            if i > 1 and nums[i-1] == nums[i-2]:
                continue
            start = nums[i-1]
            l = i
            r = len(nums) - 1
            while l < r:
                target = -start
                _sum = nums[l] + nums[r]
                if _sum == target:
                    res.append([start, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif _sum < target:
                    l += 1
                else:
                    r-= 1
            
        return res

            
        