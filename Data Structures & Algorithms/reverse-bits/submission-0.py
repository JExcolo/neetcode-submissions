class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        i = 0
        while n > 0 and i >= 0:
            if n & 1:
                res |= 1 << (31 - i)
            n = n >> 1
            i += 1

        return res
        