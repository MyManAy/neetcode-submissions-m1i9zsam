class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in range(len(nums)):
            if nums[i] in counts:
                counts[nums[i]] += 1
            else:
                counts[nums[i]] = 1

        freqs = [None] * (len(nums) + 1)
        for key, val in counts.items():
            if freqs[val]:
                freqs[val].append(key)
            else:
                freqs[val] = [key]

        res = []
        i = len(freqs) - 1
        while k > 0 and i > 0:
            while freqs[i] and len(freqs[i]) > 0:
                res.append(freqs[i].pop())
                k -=1
            i -= 1

        return res
        