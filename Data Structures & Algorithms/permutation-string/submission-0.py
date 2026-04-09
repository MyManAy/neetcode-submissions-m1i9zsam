class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1len = len(s1)
        s1count = Counter(s1)

        i = 0
        while i + s1len - 1 < len(s2):
            sub = s2[i:i+s1len]
            s2count = Counter(sub)
            if s1count == s2count:
                return True
            i += 1

        return False

        