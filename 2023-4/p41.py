'''
原地交换
'''
class Solution:
    def firstMissingPositive(self, nums) -> int:
        i = 0
        while i < len(nums):
            if 0 < nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                t = nums[i]
                nums[i] = nums[nums[i] - 1]
                nums[t - 1] = t
            else:
                i += 1
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1
        return len(nums) + 1

print(Solution().firstMissingPositive([3,4,-1,1]))