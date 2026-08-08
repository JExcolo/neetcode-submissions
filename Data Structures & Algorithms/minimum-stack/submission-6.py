class MinStack:

    def __init__(self):
        self.stack = []
        self.min_num = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min_num[-1] if self.min_num else val)
        self.min_num.append(val)
        return None
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_num.pop()
        return None
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_num[-1]
        
