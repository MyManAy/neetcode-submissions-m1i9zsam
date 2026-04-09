class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1len = len(s1)
        s2len = len(s2)

        if s2len < s1len:
            return False

        s1Counts = [0] * 26
        s2Counts = [0] * 26

        for letter in s1:
            s1Counts[ord(letter) - 97] += 1

        for i in range(s1len):
            letter = s2[i]
            s2Counts[ord(letter) - 97] += 1

        if s1Counts == s2Counts:
            return True

        i = 1
        while i + s1len - 1 < s2len:
            left = s2[i-1] 
            s2Counts[ord(left) - 97] -= 1

            letterToAdd = s2[i + s1len - 1]
            s2Counts[ord(letterToAdd) - 97] += 1

            if s1Counts == s2Counts:
                return True

            i += 1

        return False 