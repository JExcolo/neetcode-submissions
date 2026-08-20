class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        one = 1
        two = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                curr = 0
            else:
                curr = one

            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                curr += two

            two = one
            one = curr

        return one