'''
将数组一分为二，其中一定有一个是有序的，另一个可能是有序，也能是部分有序。
此时有序部分用二分法查找。无序部分再一分为二，其中一个一定有序，另一个可能有序，可能无序。就这样循环.
通过有序部分的左右判断是否在有序的里面，不在有序的里面就在无序的里面
二分记得是左边加，右边不动
'''
class Solution:
    def search(self, nums, target: int) -> int:
        first = nums[0]
        if nums[-1] > nums[0] or len(nums) == 1:
            x = -1
        else:
            left = 0
            right = len(nums) - 1
            x = (left + right) // 2
            while nums[x] < nums[0] or nums[0] < nums[x + 1]:
                if nums[x] < nums[0]:
                    right = x
                elif nums[0] < nums[x + 1]:
                    left = x + 1
                x = (left + right) // 2
        x += 1
        nums = nums[x:] + nums[:x]
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        while left < right:
            if nums[mid] == target:
                if nums[mid] >= first:
                    return (mid + x - len(nums)) % (len(nums))
                else:
                    return mid + x
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
            mid = (left + right) // 2
        if nums[mid] == target:
            if nums[mid] >= first:
                return (mid + x - len(nums)) % (len(nums))
            else:
                return mid + x
        return -1


print(Solution().search([4,5,1,2,3], 1))

