class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        longest = 1

        if len(nums) == 0:
            return 0

        for i in range(len(nums)):
            hashset.add(nums[i])


        for num in hashset:
            if  num - 1 in hashset:
                continue
            else:
                start = num
                length = 1
                while start + 1 in hashset:
                    length += 1
                    start += 1
                    longest = max(longest, length)

        return longest
        