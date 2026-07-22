class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        first_row_has_zero = 0 in matrix[0]
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(rows))

        # Step 1: Use first row and column as markers for the rest of the matrix
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # Step 2: Set inner matrix elements to zero based on markers
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Step 3: Zero out the first row and column if they originally had a zero
        if first_row_has_zero:
            matrix[0] = [0] * cols
        if first_col_has_zero:
            for r in range(rows):
                matrix[r][0] = 0