'''
enumerate(nums)是python里带下标的数组
本题我一开始的解法是先排序，再用o（1）的方式查找，题解还给出了哈希表的解法
'''
class Solution:
    def twoSum(self, nums, target: int):
        nums = sorted(enumerate(nums), key=lambda x: x[1])
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i][1] + nums[j][1] == target:
                return [nums[i][0], nums[j][0]]
            elif nums[i][1] + nums[j][1] > target:
                j -= 1
            else:
                i += 1

    def twoSumhash(self, nums, target: int):
        h = dict()
        for i, num in enumerate(nums):
            if target - num in h:
                return [h[target-num], i]
            h[num] = i
        return []