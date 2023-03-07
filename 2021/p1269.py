class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        l = min(501, arrLen)
        r = [0] * l
        s = [0] * l
        r[0] = 1
        s[0] = 1
        for i in range(steps):
            s[0] = r[0] + r[1]
            s[-1] = r[-2] + r[-1]
            for j in range(1, l - 1):
                s[j] = r[j - 1] + r[j] + r[j + 1]
            r = s.copy()
        return r[0] % (10 ** 9 + 7)


s = Solution()
print(s.numWays(6, 13))
