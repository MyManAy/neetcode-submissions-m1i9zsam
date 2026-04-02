class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        runningSum = 0
        count = 0
        for i, n in enumerate(arr):
            runningSum += n
            if i >= k - 1:
                if runningSum / k >= threshold:
                    count += 1
                runningSum -= arr[i-k+1]
        
        return count