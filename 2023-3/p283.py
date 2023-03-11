'''
依次数是第几个非零元素就行
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in nums:
            if i != 0:
                nums[j] = i
                j += 1
        while j < len(nums):
            nums[j] = 0
            j += 1

