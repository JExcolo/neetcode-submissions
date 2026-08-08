class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        targ_row = None
        s, e = 0, len(matrix) - 1
        while s <= e:
            m = (s + e) // 2
            if matrix[m][0] < target and matrix[m][-1] < target:
                s = m + 1
            elif matrix[m][0] > target and matrix[m][-1] > target:
                e = m - 1
            else:
                targ_row = m
                break

        if targ_row is None:
            return False
        
        l, r = 0, len(matrix[targ_row]) - 1

        while l <= r:
            m = (l + r) // 2
            if matrix[targ_row][m] < target:
                l = m + 1
            elif matrix[targ_row][m] > target:
                r = m - 1
            else:
                return True
        
        return False

        