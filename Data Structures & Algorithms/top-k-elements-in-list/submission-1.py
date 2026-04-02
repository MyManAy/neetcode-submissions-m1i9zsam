class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1

        freqList = [None] * (len(nums) + 1)
        for key, v in hashmap.items():
            if freqList[v]:
                freqList[v].append(key)
            else:
                freqList[v] = [key]

        i = len(freqList) - 1
        toReturn = []
        while i > 0 and k > 0:
            if freqList[i]:
                toReturn.append(freqList[i].pop())
                k -= 1
            else:
                i -= 1

        return toReturn

        