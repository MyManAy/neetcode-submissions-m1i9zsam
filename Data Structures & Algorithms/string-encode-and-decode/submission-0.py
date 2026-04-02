class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in range(len(strs)):
            length = len(strs[i])
            seperator = "@"
            encoded += str(length) + seperator + strs[i]

        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        builtNum = ""
        digits = "0123456789"
        decoded = []
        i = 0
        while i < len(s):
            while s[i] in digits:
                builtNum += s[i]
                i+=1
            i+=1
            toConsume = int(builtNum)
            j = i
            builtStr = ""
            while j < i + toConsume :
                builtStr += s[j]
                j += 1
            decoded.append(builtStr)
            i += toConsume
            builtNum = ""

        return decoded
