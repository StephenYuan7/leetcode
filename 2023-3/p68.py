class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        r = [1 for i in range(n)]
        for i in range(m - 1):
            for j in range(n):
                if j == 0:
                    r[j] = 1
                else:
                    r[j] += r[j - 1]
        return r[-1]


print(Solution().uniquePaths(3, 3))