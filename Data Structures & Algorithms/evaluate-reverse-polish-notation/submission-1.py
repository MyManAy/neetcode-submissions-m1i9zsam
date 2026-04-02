class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"*", "+", "/", "-"}
        for i in range(len(tokens)):
            token = tokens[i]

            if token not in operations:
                stack.append(token)
            else:
                second = int(stack.pop())
                first = int(stack.pop())
                result = None
                if token == "*":
                    result = first * second
                elif token == "/":
                    result = first / second
                elif token == "+":
                    result = first + second
                else:
                    result = first - second

                stack.append(result)

        return int(stack.pop())




         