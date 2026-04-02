class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ("(", "[", "{")
        closing = (")", "]", "}")
        openingDict = {opening[i]: closing[i] for i in range(len(opening))}

        for i in range(len(s)):
            if s[i] in openingDict:
                stack.append(s[i])
                continue
            else:
                if stack and openingDict[stack[-1]] == s[i]:
                    stack.pop()
                    continue
                else:
                    return False 

        if len(stack) > 0:
            return False
        return True
        