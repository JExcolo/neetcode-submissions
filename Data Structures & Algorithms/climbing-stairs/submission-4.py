class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 0

        for _ in range(n):
            temp = one
            one = one + two
            two = temp
        
        return one