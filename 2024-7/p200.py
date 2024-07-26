class Solution:
    def numIslands(self, grid) -> int:
        r = 0
        t = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    r += 1
                    grid[i][j] = 2
                    t.append((i, j))
                    while t:
                        x = t.pop()
                        for a, b in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            if 0 <= x[0] + a < len(grid) and 0 <= x[1] + b < len(grid[0]):
                                if grid[x[0] + a][x[1] + b] == '1':
                                    grid[x[0] + a][x[1] + b] = 2
                                    t.append((x[0] + a, x[1] + b))
        return r

print(Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))