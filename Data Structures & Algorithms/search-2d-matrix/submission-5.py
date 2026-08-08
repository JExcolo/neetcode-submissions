class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix) - 1
    

        while top <= bot:
            row = (top + bot) // 2
            if(target > matrix[row][-1]):
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        for i in range(len(matrix)):
            if (matrix[i][-1] >= target):
                l = 0
                r = len(matrix[i]) - 1
                while l <= r:
                    m = (l + r) // 2
                    if(matrix[i][m] == target):
                        return True
                    elif (matrix[i][m] < target):
                        l  = m + 1
                        continue
                    else:
                        r = m - 1
                        continue
                return False
            else:
                continue
        return False        
        