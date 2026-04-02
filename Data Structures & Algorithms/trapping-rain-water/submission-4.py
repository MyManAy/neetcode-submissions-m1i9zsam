class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = [0] * len(height)
        maxR = [0] * len(height)

        largest = 0
        for i in range(len(height)):
            maxL[i] = largest
            largest = max(largest, height[i])

        largest = 0
        for i in range(len(height) - 1, -1, -1):
            maxR[i] = largest
            largest = max(largest, height[i])

        water = 0
        for i in range(len(height)):
            container = min(maxR[i], maxL[i])
            
            toAdd = container - height[i]
            if toAdd > 0:
                water += toAdd

        return water
        
        