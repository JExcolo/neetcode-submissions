from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                if grid[r][c] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        moves = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
            ]
        
        while q:
            x, y, time = q.popleft()
            for dx, dy in moves:
                nr, nc = x + dx, y + dy
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                    q.append((nr, nc, time + 1))
                    grid[nr][nc] = 2
                    fresh -= 1
                    if fresh == 0:
                        return time + 1
        
        return -1




        