class Solution:
    def searchRange(self, nums, target: int):
        left = 0
        right = len(nums) - 1
        if right < 0:
            return [-1, -1]
        mid = (left + right) // 2
        while left < right:
            if nums[mid] == target:
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
            mid = (left + right) // 2
        if nums[mid] != target:
            return [-1, -1]
        left_left = left
        left_right = mid
        left_mid = (left_left + left_right) // 2
        while left_left < left_right:
            if nums[left_mid] == target:
                left_right = left_mid
            else:
                left_left = left_mid + 1
            left_mid = (left_left + left_right) // 2
        right_left = mid
        right_right = right
        right_mid = (right_left + right_right + 1) // 2
        while right_left < right_right:
            if nums[right_mid] == target:
                right_left = right_mid
            else:
                right_right = right_mid - 1
            right_mid = (right_left + right_right + 1) // 2

        return [left_right, right_left]


print(Solution().searchRange([], 6))
