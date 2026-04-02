class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zeroCount = 0
        for i in range(len(nums)):
            n = nums[i]
            if n == 0:
                zeroCount += 1
                continue
            total *= n
        
        toReturn = []
        if zeroCount > 1:
            for i in range(len(nums)):
                toReturn.append(0)
        elif zeroCount == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    toReturn.append(total)
                else:
                    toReturn.append(0)
        else:
            for i in range(len(nums)):
                toReturn.append(total // nums[i])
        
        return toReturn
            