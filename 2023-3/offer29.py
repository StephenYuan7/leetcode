class Solution:
    def spiralOrder(self, matrix):
        top = 0
        bottom = len(matrix)
        if bottom == 0:
            return []
        left = 0
        right = len(matrix[0])
        if right == 0:
            return []
        r = []
        while left < right and top < bottom:
            for i in range(left, right):
                r.append(matrix[top][i])
            top = top + 1
            if top == bottom:
                break
            for i in range(top, bottom):
                r.append(matrix[i][right-1])
            right = right - 1
            if right == left:
                break
            for i in range(right-1, left-1, -1):
                r.append(matrix[bottom-1][i])
            bottom = bottom - 1
            if bottom == top:
                break
            for i in range(bottom-1, top-1, -1):
                r.append(matrix[i][left])
            left = left + 1
        return r


print(Solution().spiralOrder([[1,2,3,4],
                              [5,6,7,8],
                              [9,10,11,12]]))