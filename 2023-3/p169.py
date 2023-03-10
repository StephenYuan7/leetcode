'''
最容易的暴力哈希表
题解用了选举的方法
'''
class Solution:
    def majorityElement(self, nums) -> int:
        r = {}
        for num in nums:
            if num in r:
                r[num] += 1
            else:
                r[num] = 1
            if r[num] > len(nums) / 2:
                return num

    def solution(self,nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

Solution().majorityElement([3,2,3])
