class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def rec(built, i):
            if not i < len(nums):
                res.append(built[:])
                return

        
            built.append(nums[i])
            rec(built, i+1)

            built.pop()
            rec(built, i+1)

            return

        rec([], 0)
        return res
            

        