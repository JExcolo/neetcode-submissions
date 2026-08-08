from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = deque()
        start = (sr, sc)
        ogColor = image[sr][sc]
        q.append(start)
        visited = set()
        moves = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        while q:
            x, y = q.popleft()
            if image[x][y] == ogColor and (x, y) not in visited:
                image[x][y] = color
                for move in moves:
                    dX, dY = move
                    r_bound = 0 <= x + dX < len(image)
                    c_bound = 0 <= y + dY < len(image[0])
                    if r_bound and c_bound:
                        q.append((x + dX, y + dY))
            visited.add((x, y))
        return image
