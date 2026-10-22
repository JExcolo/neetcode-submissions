class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        moves = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]
        def dfs(grid, x, y, visited):
            xB = 0 <= x < len(grid)
            yB = 0 <= y < len(grid[0])

            if not xB or not yB or (x, y) in visited or grid[x][y] == 1:
                return 0
            
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return 1
            
            visited.add( (x, y) )
            count = 0
            for dX, dY in moves:
                count += dfs(grid, x + dX, y + dY, visited)
            
            visited.remove( (x, y) )
            return count
        
        return dfs(grid, 0, 0, set())