class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        res = []
        for string in strs:
            counts = [0] * 26

            for c in string:
                counts[ord(c) - ord('a')] += 1

            counts = tuple(counts)
            if counts in hashmap:
                res[hashmap[counts]].append(string)
            else:
                res.append([string])
                hashmap[counts] = len(res) - 1

        return res

        