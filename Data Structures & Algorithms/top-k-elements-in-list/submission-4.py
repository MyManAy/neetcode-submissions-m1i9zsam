class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        
        freqs = [None] * len(nums)
        for key,v in counts.items():
            if freqs[v-1] is None:
                freqs[v-1] = [key]
            else:
                freqs[v-1].append(key)

        res = []
        for i in range(len(freqs) - 1, -1, -1):
            while freqs[i] and k > 0: 
                res.append(freqs[i].pop())
                k -= 1
            if k <= 0:
                return res

        return res
        

        