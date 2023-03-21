class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def exchange(i, j):
            matrix[i][j], matrix[j][len(matrix) - 1 - i], \
            matrix[len(matrix) - 1 - i][len(matrix) - 1 - j], matrix[len(matrix) - 1 - j][i] \
                = matrix[len(matrix) - 1 - j][i], matrix[i][j], matrix[j][len(matrix) - 1 - i], \
                    matrix[len(matrix) - 1 - i][len(matrix) - 1 - j]

        for i in range(len(matrix) // 2):
            for j in range(len(matrix) // 2):
                exchange(i, j)
        if len(matrix) % 2 == 1:
            for j in range(len(matrix) // 2):
                exchange(len(matrix) // 2, j)
        return matrix


print(Solution().rotate([[1,2,3],[4,5,6],[7,8,9]]))
