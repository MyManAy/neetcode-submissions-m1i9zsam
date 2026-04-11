class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def rec(built, total, i):
            if not i < len(nums):
                return

            if total > target:
                return

            if total == target:
                res.append(built[:])
                return

            built.append(nums[i])
            total += nums[i]
            rec(built, total, i)

            built.pop()
            total -= nums[i]
            rec(built, total, i+1)

            return

        rec([], 0, 0)
        return res
        