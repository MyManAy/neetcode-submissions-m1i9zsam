class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largest = 0
        for i, h in enumerate(heights):
            if len(stack) == 0:
                stack.append((i, h))
                continue
            
            idx, height = stack[len(stack) - 1]
            if h >= height:
                stack.append((i, h))
            else:
                while stack and h < stack[-1][1]:
                    idx, height = stack.pop()
                    area = (i - idx) * height
                    largest = max(area, largest)
                stack.append((idx, h))

        while stack:
            idx, height = stack.pop()
            area = (len(heights) - idx) * height
            largest = max(area, largest)

        return largest


        
        