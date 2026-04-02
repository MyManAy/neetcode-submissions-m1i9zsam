class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            t = temperatures[i]
            while len(stack) > 0 and t > temperatures[stack[len(stack) - 1]]:
                index = stack.pop()
                res[index] += i - index
            stack.append(i)

        return res

        
        