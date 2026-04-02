class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        largest = float("-inf")

        while l < r:
            minHeight = min(heights[l], heights[r])
            area = (r - l) * minHeight

            if area > largest:
                largest = area

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return largest