class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == "[":
                stack.append("[")
            elif s[i] == "(":
                stack.append("(")
            elif s[i] == "{":
                stack.append("{")
            elif s[i] == "}":
                if not stack or stack.pop() != "{":
                    return False
            elif s[i] == ")":
                if not stack or stack.pop() != "(":
                    return False
            elif s[i] == "]":
                if not stack or stack.pop() != "[":
                    return False
        return len(stack) == 0
