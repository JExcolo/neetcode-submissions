class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = set()
        maxArea = 0
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
                if 0 <= r + x < n and 0 <= c + y < m:
                    total += dfs(r + x, c + y)
            return total

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                maxArea = max(maxArea, dfs(r, c))
        
        return maxArea
                
