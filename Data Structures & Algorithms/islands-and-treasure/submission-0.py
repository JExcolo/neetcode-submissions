from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        q = deque()

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 0:
                    q.append((0, r, c))
                    visited.add((r, c))
                elif grid[r][c] == -1:
                    visited.add((r, c))
        
        moves = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while q:
            step, r, c = q.popleft()
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                rBounds = 0 <= nr < len(grid)
                cBounds = 0 <= nc < len(grid[r])
                if rBounds and cBounds and (nr, nc) not in visited and grid[nr][nc] != -1:
                    grid[nr][nc] = step + 1
                    q.append(( step + 1, nr, nc ))
                    visited.add(( nr, nc ))
        
