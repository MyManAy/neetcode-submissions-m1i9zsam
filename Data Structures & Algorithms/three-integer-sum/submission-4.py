class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        i = 0
        while i < len(nums) - 2:
            start = nums[i]
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                target = -start
                _sum = nums[l] + nums[r]
                if _sum == target:
                    res.append([start, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                elif _sum < target:
                    l += 1
                else:
                    r -= 1

            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i-1]:
                i += 1

            

        return res


        