class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        alt = set()
        m = len(heights)
        n = len(heights[0])

        def dfs(r, c, h, ocean):
            if r < 0 or c < 0 or r >= m or c >= n:
                return
            if (r, c) in ocean or heights[r][c] < h:
                return

            ocean.add((r, c))
            moves = [
                (0, -1),
                (-1, 0),
                (1, 0),
                (0, 1),
            ]
            curH = heights[r][c]

            for dx, dy in moves:
                dfs(r + dx, c + dy, curH, ocean)

        for c in range(n):
            dfs(0, c, 0, pac)
        for r in range(m):
            dfs(r, 0, 0, pac)
        for c in range(n):
            dfs(m - 1, c, 0, alt)
        for r in range(m):
            dfs(r, n - 1, 0, alt)
        
        res = []
        for r in range(m):
            for c in range(n):
                if (r, c) in pac and (r, c) in alt:
                    res.append([r, c])

        return res