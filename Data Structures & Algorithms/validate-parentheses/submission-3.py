class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        closers = {")": "(", "}": "{", "]": "["}
        stack = []
        for i in s:
            if i in closers:
                if stack and stack[-1] == closers[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if len(stack) == 0:
            return True
        else:
            return False

