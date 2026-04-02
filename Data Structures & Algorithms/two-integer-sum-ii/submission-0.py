class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1

        while L < R:
            _sum = numbers[L] + numbers[R]
            if _sum > target:
                R -= 1
            elif _sum < target:
                L += 1
            else:
                return [L+1, R+1]
        
        return 
        