class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        counter = Counter(nums)

        if counter.most_common(1)[0][1] > 1:
            return True
        return False

        