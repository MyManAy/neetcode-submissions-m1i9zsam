class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        firstpass = [1]
        for i in range(1, len(nums)):
            firstpass.append(nums[i-1] * firstpass[len(firstpass) - 1])
        
        secondpass = [1]
        for i in range(len(nums) - 2, -1, -1):
            secondpass.append(nums[i+1] * secondpass[len(secondpass) - 1])

        secondpass.reverse()

        res = []
        for i in range(len(nums)):
            res.append(firstpass[i] * secondpass[i])
        
        return res

            