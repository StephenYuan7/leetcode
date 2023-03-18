'''
两数交换 a,b = b,a
'''

class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        max_stat = nums[-1]
        i = len(nums) - 2
        while i >= 0:
            if nums[i] >= max_stat:
                max_stat = nums[i]
            else:
                break
            i -= 1
        left = i + 1
        right = len(nums) - 1
        while right > left:
            nums[right], nums[left] = nums[left], nums[right]
            right -= 1
            left += 1
        if i > -1:
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
        return nums


print(Solution().nextPermutation([1, 3, 2]))