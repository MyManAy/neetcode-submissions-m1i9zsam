class Solution:
    def trap(self, height: List[int]) -> int:
        lscan = [0] * len(height)
        rscan = [0] * len(height)

        largest = 0
        for i in range(len(height)):
            lscan[i] = largest
            largest = max(height[i], largest)

        largest = 0
        for i in range(len(height) - 1, -1, -1):

            rscan[i]=largest
            largest = max(height[i], largest)

        total = 0
        for i in range(len(height)):
            l = min(lscan[i], rscan[i])

            toAdd= l - height[i]
            if toAdd > 0:
                total += toAdd

        return total

        
        