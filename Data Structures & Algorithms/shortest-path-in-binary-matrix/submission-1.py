from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        moves = [
            (1, 0), # down
            (-1, 0), # Up
            (1, 1), # down-right
            (1, -1), # down-left
            (-1, -1), #up-left
            (-1, 1), # up-right
            (0, 1),
            (0, -1)
        ]
        q = deque()
        visited = set()
        q.append((0, 0, 1))
        while q:
            r, c, steps = q.popleft()
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return steps
            if grid[r][c] == 1 or (r, c) in visited:
                continue
            visited.add((r, c))
            for dx, dy in moves:
                nr, nc = r + dx, c + dy
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    q.append((nr, nc, steps + 1))
            
        return -1