class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter
        res = []
        hashmap = {}
        for i in range(len(strs)):
            string = strs[i]
            count = Counter(string)
            immutable = frozenset(count.items())

            if immutable in hashmap:
                res[hashmap[immutable]].append(string)
            else:
                res.append([string])
                hashmap[immutable] = len(res) - 1

        return res

        