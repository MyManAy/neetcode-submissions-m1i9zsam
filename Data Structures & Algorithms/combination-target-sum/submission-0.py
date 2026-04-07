class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def rec(path, i, total):
            if not i < len(nums):
                return

            if total == target:
                res.append(path[:])
                return
            if total > target:
                return

            total += nums[i]
            path.append(nums[i])
            rec(path, i, total)

            total -= nums[i]
            path.pop()
            rec(path, i+1, total)

        rec([], 0, 0)
        return res
        