class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def rec(path, i):
            if not i < len(nums):
                res.append(path[:])
                return

            path.append(nums[i])
            rec(path, i + 1)
            path.pop()
            rec(path, i + 1)

        rec([], 0)
        return res
        