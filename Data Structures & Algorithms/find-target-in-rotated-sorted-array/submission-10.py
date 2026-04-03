class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        pivot = l
        while l <= r:
            if nums[l] <= nums[r]:
                pivot = l
                break

            m = (l+r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        l  = 0
        r = len(nums) -1
        while l <= r:
            m = (l+r) // 2
            m2 = (m + pivot) % len(nums)

            if target > nums[m2]:
                l = m + 1
            elif target < nums[m2]:
                r = m - 1
            else:
                return m2

        return -1
        