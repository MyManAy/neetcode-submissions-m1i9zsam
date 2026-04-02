class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        posTime = []
        for i in range(len(position)):
            t = (target - position[i]) / speed[i]
            posTime.append((position[i], t))

        posTime.sort(key=lambda x: -x[0])


        stack = []
        for p, t in posTime:
            if len(stack) == 0:
                stack.append((p, t))
                continue

            if t <= stack[len(stack) - 1][1]:
                continue
            else:
                stack.append((p, t))

        return len(stack)

            


        