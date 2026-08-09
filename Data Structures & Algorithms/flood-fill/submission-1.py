from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = deque()
        start = (sr, sc)
        ogColor = image[sr][sc]
        if ogColor == color:
            return image
        image[sr][sc] = color
        q.append(start)
        moves = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        while q:
            x, y = q.popleft()
            for move in moves:
                dX, dY = move
                r_bound = 0 <= x + dX < len(image)
                c_bound = 0 <= y + dY < len(image[0])
                if r_bound and c_bound and image[x + dX][y + dY] == ogColor:
                    image[x + dX][y + dY] = color
                    q.append((x + dX, y + dY))
        return image
