class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        nums.sort()
        r = [0] * (target + 1)
        r[0] = 1
        for i in range(target + 1):
            for j in range(i):
                for k in nums:
                    x = k + j
                    if x == i:
                        r[i] += r[j]
                    elif x > i:
                        break
        return r[target]


s = Solution()
print(s.combinationSum4([1, 2, 3], 4))
