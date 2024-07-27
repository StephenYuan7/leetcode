class Solution:
    def permute(self, nums):
        if len(nums) == 1:
            return [nums]
        r = []
        for i in range(len(nums)):
            t = nums.copy()
            x = t.pop(i)
            a = self.permute(t)
            for j in a:
                j.append(x)
            r.extend(a)
        return r

print(Solution().permute([1]))