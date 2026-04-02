class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        res = []
        
        for string in strs:
            counts = [0] * 26
            for c in string:
                counts[ord(c) - ord('a')] += 1
            
            immutable = tuple(counts)
            if immutable in hashmap:
                res[hashmap[immutable]].append(string)
            else:
                res.append([string])
                hashmap[immutable] = len(res) - 1

        return res

        