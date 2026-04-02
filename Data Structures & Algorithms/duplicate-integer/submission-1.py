class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)

        for k, v in counter.items():
            if v > 1:
                return True

        return False

        