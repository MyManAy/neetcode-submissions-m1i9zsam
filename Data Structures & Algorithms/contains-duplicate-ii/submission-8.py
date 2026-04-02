class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = set()
        if k == 0:
            return False
        L = 0
        R = 1
        print(len(nums)-k)
        while True:
            mapping.add(nums[L])
            if R >= len(nums):
                return False
            while R - L <= k:
                if nums[R] in mapping:
                    return True
                mapping.add(nums[R])
                R += 1
            mapping.remove(nums[L])
            L += 1
        return False
                
        