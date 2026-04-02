class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mapping = {}
        def rec(index):
            if index == len(nums) - 1:
                return True
            if index in mapping:
                return mapping[index]
            jumps = nums[index]
            if jumps == 0:
                return False
            
            can = False
            for i in range(1, jumps+1):
                if rec(index + i):
                    can = True
                    break
            mapping[index] = can
            return can
        
        return rec(0)
            
