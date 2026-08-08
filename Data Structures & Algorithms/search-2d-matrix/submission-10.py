class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        targ_row = None
        for i in range(len(matrix)):
            if target == matrix[i][0] or target == matrix[i][-1]:
                return True
            if target >= matrix[i][0] and target <= matrix[i][-1]:
                targ_row = i
        
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

        