from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        islands = set()
        q = deque()

        for c in range(0, n):
            if board[0][c] == "O":
                q.append( (0, c) )
        for c in range(0, n):
            if board[m - 1][c] == "O":
                q.append( (m - 1, c) )
        for r in range(0, m):
            if board[r][0] == "O":
                q.append( (r, 0) )
        for r in range(0, m):
            if board[r][n - 1] == "O":
                q.append( (r, n - 1) )

        moves = [
            (0, 1),
            (1, 0),
            (-1, 0),
            (0, -1)
        ]
        while q:
            x, y = q.popleft()
            if (x, y) in islands:
                continue
            islands.add((x, y))
            for dx, dy in moves:
                nr, nc = x + dx, y + dy
                rB = 0 <= nr < m
                rC = 0 <= nc < n
                if rB and rC and board[nr][nc] == "O" and (nr, nc) not in islands:
                    q.append((nr, nc))



        for r in range(m):
            for c in range(n):
                if board[r][c] == "O" and (r, c) not in islands:
                    board[r][c] = "X"
        
