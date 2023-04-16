'''
注意前缀和
'''

class Solution:
    def subarraySum(self, nums, k):
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
        res = {0: 1}
        r = 0
        for i in nums:
            if i - k in res:
                r += res[i - k]
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
        return r


print(Solution().subarraySum([1,1,1], 2))