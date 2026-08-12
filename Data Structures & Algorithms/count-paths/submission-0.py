class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevR = [0] * n

        for r in range(m - 1, -1, -1):
            curR = [0] * n
            curR[n - 1] = 1
            for c in range(n - 2, -1, -1):
                curR[c] = curR[c + 1] + prevR[c]
            prevR = curR
        
        return prevR[0]

        