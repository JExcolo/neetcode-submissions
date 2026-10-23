from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        visited = set()
        q = deque([])
        q.append((0, 0, 0))

        moves = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while q:
            x, y, move = q.popleft()
            if grid[x][y] == 1 or (x, y) in visited:
                continue
            
            if (x, y) == (len(grid) - 1, len(grid[0]) - 1):
                return move
            
            visited.add((x, y))
            for dX, dY in moves:
                nX, nY = x + dX, y + dY
                rB = 0 <= nX < len(grid)
                cB = 0 <= nY < len(grid[0])
                
                if not rB or not cB:
                    continue
                q.append( (nX, nY, move + 1))
        
        return -1