class MinStack:

    def __init__(self):
        self.minStack = []
        self.stack = []
        

    def push(self, val: int) -> None:
        minStack = self.minStack
        stack = self.stack
        if not minStack or val < minStack[-1]:
            minStack.append(val)
        else:
            minStack.append(minStack[-1])

        stack.append(val)

        

    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
