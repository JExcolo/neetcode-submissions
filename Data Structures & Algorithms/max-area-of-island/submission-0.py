class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = set()
        maxArea = float("-inf")
        moves = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        def dfs(r, c):
            if grid[r][c] == 0 or (r, c) in visited:
                return 0
            visited.add((r, c))
            total = 1
            for x, y in moves:
                nr, nc = r + x, c + y
                rB = 0 <= nr < n
                rC = 0 <= nc < m
                if rB and rC:
                    total += dfs(nr, nc)
            
            return total

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                found = dfs(r, c)
                maxArea = max(maxArea, found)
        
        return maxArea if maxArea != float("-inf") else 0
                
