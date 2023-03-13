class Solution:
    def findNumberIn2DArray(self, matrix, target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        if matrix[0][0] > target:
            return False
        for i in range(m):
            left = 0
            right = n - 1
            while left < right:
                mid = (left + right) // 2
                if matrix[i][mid] == target:
                    return True
                if matrix[i][mid] < target:
                    left = mid + 1
                else:
                    right = mid
            if matrix[i][left] == target:
                return True
        return False

    def solution(self, matrix, target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        x = 0
        y = n - 1
        while x < m-1 or y > 0:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                x += 1
                if x > m-1:
                    return False
            else:
                y -= 1
                if y < 0:
                    return False
        if matrix[x][y] == target:
            return True
        return False


print(Solution().solution(
    [[-1,3]], -1))
