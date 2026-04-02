class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recSearch(nums, target, l, r):
            m = (l + r) // 2

            if r < l:
                return -1

            if target < nums[m]:
                return recSearch(nums, target, l, m-1)
            elif target > nums[m]:
                return recSearch(nums, target, m+1, r)
            else:
                return m

        return recSearch(nums, target, 0, len(nums)-1)
        

            
        