class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for letter in s:
            if letter == ")":
                if len(stack) == 0:
                    return False
                if stack[len(stack) - 1] == "(":
                    stack.pop()
                else:
                    return False
            elif letter == "}":
                if len(stack) == 0:
                    return False
                if stack[len(stack) - 1] == "{":
                    stack.pop()
                else:
                    return False
            elif letter == "]":
                if len(stack) == 0:
                    return False
                if stack[len(stack) - 1] == "[":
                    stack.pop()
                else:
                    return False
            else:
                stack.append(letter)
        if len(stack) != 0:
            return False
        return True