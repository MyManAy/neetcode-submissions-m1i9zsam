class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if len(stack) == 0:
                stack.append(i)
                continue

            while stack and temperatures[i] > temperatures[stack[len(stack) - 1]]:
                ti = stack.pop()
                res[ti] = i - ti

            stack.append(i)

        return res


        