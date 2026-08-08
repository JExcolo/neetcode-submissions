class MinStack:

    def __init__(self):
        self.stack = []
        self.min_num = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_num or val <= self.getMin():
            self.min_num.append(val)
        return None
        

    def pop(self) -> None:
        num = self.stack.pop()
        if num == self.getMin():
            self.min_num.pop()
        return None
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_num[-1]
        
