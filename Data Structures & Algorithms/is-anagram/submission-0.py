class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        sCounter = Counter(s)
        tCounter = Counter(t)

        if sCounter == tCounter:
            return True
        else:
            return False
        