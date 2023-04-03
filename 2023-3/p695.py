'''
深度优先遍历
也可以考虑用栈与队列
'''
class Solution:
    def maxAreaOfIsland(self, grid):
        def dfs(a, b):
            if a < 0 or a >= len(grid) or b < 0 or b >= len(grid[0]) or grid[a][b] == 0:
                return 0
            r = 1
            grid[a][b] = 0
            for t in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                r += dfs(a + t[0], b + t[1])
            return r

        m = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                m = max(m, dfs(i, j))
        return m
