class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        # handle empty matrix
        if not matrix or not matrix[0]:
            self.P = [[0]]
            return

        m, n = len(matrix), len(matrix[0])
        # Build prefix matrix of size (m+1) x (n+1)
        self.P = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                self.P[i + 1][j + 1] = (
                    matrix[i][j]
                    + self.P[i][j + 1]
                    + self.P[i + 1][j]
                    - self.P[i][j]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # inclusion-exclusion formula
        return (
            self.P[row2 + 1][col2 + 1]
            - self.P[row1][col2 + 1]
            - self.P[row2 + 1][col1]
            + self.P[row1][col1]
        )