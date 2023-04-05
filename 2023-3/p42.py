'''
最朴素的方法做了一个，还可以动态规划
'''
class Solution:
    def trap(self, height) -> int:
        left = 0
        right = len(height) - 1
        r = 0
        x = 0
        while left < right:
            while left < right and (height[left] < x or height[left] <= height[left + 1]):
                left += 1
            while left < right and (height[right] < x or height[right] <= height[right - 1]):
                right -= 1
            x = min(height[left], height[right])
            for i in range(left, right):
                if height[i] < x:
                    r += x - height[i]
                    height[i] = x
            x += 1
        return r

    def trap2(self, height):
        r = 0
        left = [0] * len(height)
        right = [0] * len(height)
        for i in range(len(height) - 1):
            left[i + 1] = max(left[i], height[i])
        for i in range(len(height) - 1, 0, -1):
            right[i - 1] = max(right[i], height[i])
        for i in range(len(height)):
            if height[i] < min(left[i], right[i]):
                r += min(left[i], right[i]) - height[i]
        return r


print(Solution().trap2([4,2,0,3,2,5]))