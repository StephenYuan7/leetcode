'''
从开始遍历，碰到和为正数就继续，为负数就重新开始
'''

class Solution:
    def maxSubArray(self, nums) -> int:
        r = nums[0]
        a = 0
        for i in nums:
            if i >= 0:
                if a >= 0:
                    a = a + i
                else:
                    a = i
            else:
                if i + a > 0:
                    a = i + a
                else:
                    a = i
            r = max(r, a)
        return r
