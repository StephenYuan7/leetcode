class Solution:
    def maxScore(self, nums):
        def my(x, y, z, n):
            r = 0
            a = 0
            for i in y:
                if i == 0:
                    a = 1
                    break
            if a == 0:
                z.sort()
                for i in range(n):
                    r += (i + 1) * z[i]
                return r
            for i in range(2 * n):
                for j in range(i + 1, 2 * n):
                    if y[i] == 0 and y[j] == 0:
                        zt = z[:]
                        zt.append(x[i][j])
                        yt = y[:]
                        yt[i] = 1
                        yt[j] = 1
                        t = my(x, yt, zt, n)
                        if t > r:
                            r = t
            return r

        x = []
        y = []
        n = len(nums)
        for i in range(n):
            y.append(0)
            xt = []
            for j in range(n):
                # xt.append(gcd(nums[i], nums[j]))
                xt.append(1)
            x.append(xt)
        return my(x, y, [], n // 2)

s = Solution()
print(s.maxScore([773274,313112,131789,222437,918065,49745,321270,74163,900218,80160,325440,961730]))