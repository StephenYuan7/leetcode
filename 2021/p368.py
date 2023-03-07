class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        l = len(nums)
        f = [0] * l
        g = [0] * l
        maxlen = 0
        for i in range(l):
            a = 1
            b = -1
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if f[j] + 1 >= a:
                        a = f[j] + 1
                        b = j
            f[i] = a
            g[i] = b
        maxlen = f.index(max(f))
        r = []
        while maxlen != -1:
            r.append(nums[maxlen])
            maxlen = g[maxlen]
        return r


s = Solution()
my_nums = [343, 49, 8, 4, 2, 1]
print(s.largestDivisibleSubset(my_nums))
