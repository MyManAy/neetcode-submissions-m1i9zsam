class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = float("-inf")
        l = 0
        r = len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            largest = max(largest, area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return largest

        