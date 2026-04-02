class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in range(len(nums)):
            if nums[i] in counts:
                counts[nums[i]] += 1
            else:
                counts[nums[i]] = 1
        
        frequencies = [None] * (len(nums) + 1)
        for key,val in counts.items():
            if frequencies[val]:
                frequencies[val].append(key)
            else:
                frequencies[val] = [key]

        res = []
        i = len(frequencies) - 1
        while i > 0 and k > 0:
            if frequencies[i]:
                res.append(frequencies[i].pop())
                k -= 1
            else:
                i -= 1

        return res

        