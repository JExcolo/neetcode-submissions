from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        moves = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        islands = 0
        def dfs(r, c, visited):
            for dr, dc, in moves:
                nr, nc = r + dr, c + dc
                r_b = 0 <= nr < len(grid)
                c_b = 0 <= nc < len(grid[0])
                if r_b and c_b and grid[nr][nc] == "1" and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    dfs(nr, nc, visited)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visited and grid[r][c] == "1":
                    dfs(r, c, visited)
                    islands += 1
        return islands


