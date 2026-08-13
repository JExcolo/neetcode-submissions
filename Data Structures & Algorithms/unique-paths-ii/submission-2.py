class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        lR, lC = len(obstacleGrid), len(obstacleGrid[0])
        prevR = [0] * lC
        for r in range(lR - 1, -1, -1):
            curR = [0] * lC
            if r == lR - 1:
                curR[lC - 1] = 1
            elif r + 1 <= lR - 1:
                curR[lC - 1] = prevR[-1]
            
            if obstacleGrid[r][lC - 1] == 1:
                curR[lC - 1] = 0
                
            for c in range(lC - 2, -1, -1):

                if obstacleGrid[r][c] == 1:
                    curR[c] = 0
                else:
                    curR[c] = curR[c + 1] + prevR[c]
            prevR = curR
            if r == lR - 1 and obstacleGrid[r][-1] != 1:
                prevR[-1] = 1
        return prevR[0]
        