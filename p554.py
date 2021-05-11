class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        n = len(wall)
        w = sum(wall[0])
        r = {0: 0}
        for i in wall:
            s = 0
            for j in i:
                s += j
                if s in r:
                    r[s] += 1
                else:
                    r[s] = 1
        del r[w]
        x = max(r.values())
        return n - x


s = Solution()
print(s.leastBricks([[1,1],[2],[1,1]]))
