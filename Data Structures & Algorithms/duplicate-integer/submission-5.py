class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        counter = Counter(nums)

        toReturn = True if counter.most_common(1)[0][1] > 1 else False
        return toReturn

        