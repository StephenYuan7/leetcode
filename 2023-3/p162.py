'''
二分二分！！！
'''
class Solution:
    def findPeakElement(self, nums) -> int:
        if len(nums) <= 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1
        left = 0
        right = len(nums) - 1
        while 1:
            mid = (right + left) // 2
            if nums[mid - 1] < nums[mid]:
                if nums[mid] > nums[mid + 1]:
                    return mid
                else:
                    left = mid + 1
            else:
                right = mid