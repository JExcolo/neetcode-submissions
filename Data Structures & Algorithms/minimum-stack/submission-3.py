class MinStack:

    def __init__(self):
        self.stack = []
        self.currMin = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if (len(self.currMin) == 0 or self.currMin[-1] >= val):
            self.currMin.append(val)
        

    def pop(self) -> None:
        if(self.currMin[-1] == self.top()):
            self.currMin.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]
        

    def getMin(self) -> int:
        if(len(self.currMin) == 0):
            return None
        return self.currMin[-1]
