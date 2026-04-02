class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recSearch(nums, target, l, r):
            if r < l:
                return -1
            
            m = (l + r) // 2

            if target > nums[m]:
                return recSearch(nums, target, m+1, r)
            elif target < nums[m]:
                return recSearch(nums, target, l, m-1)
            else:
                return m

        return recSearch(nums, target, 0, len(nums)-1)

            
        