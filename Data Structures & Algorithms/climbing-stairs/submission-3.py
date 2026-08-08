class Solution:
    def climbStairs(self, n: int) -> int:
        return self._climbStairs(n, {})
        
    def _climbStairs(self, n: int, memo : dict) -> int:
        if n <= 2:
            return n
        if n in memo:
            return memo[n]
        
        one_step = self._climbStairs(n - 1, memo)
        two_step = self._climbStairs(n - 2, memo)

        memo[n] = one_step + two_step
        return memo[n]