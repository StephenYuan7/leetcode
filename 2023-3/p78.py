class Solution:
    def subsets(self, nums):
        r = [[]]
        for i in range(pow(2, len(nums))):
            x = []
            for j in range(len(nums)):
                if i % pow(2, j + 1) // pow(2, j) == 1:
                    x.append(nums[j])
            if x:
                r.append(x)
        return r


print(Solution().subsets([0]))