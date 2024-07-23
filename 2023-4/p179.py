'''
比较的时候也可以直接比较a+b与b+a的大小即可
'''
class Solution:
    def largestNumber(self, nums):
        def compare_big(a, b):
            for i in range(min(len(a), len(b))):
                if a[i] > b[i]:
                    return True
                if a[i] < b[i]:
                    return False
            if len(a) > len(b):
                return compare_big(a[len(b):], b)
            elif len(a) < len(b):
                return compare_big(a, b[len(a):])
            return True

        def quicksort(left, right):
            x = [(left, right)]
            while x:
                left, right = x.pop()
                if left < right:
                    t = 0
                    for i in range(left, right + 1):
                        if nums[i] != nums[left]:
                            t = 1
                            break
                    if t:
                        nums[left], nums[left + (right - left) // 3] = nums[left + (right - left) // 3],  nums[left]
                        a = left + 1
                        b = right
                        while a < b:
                            while a < b and compare_big(nums[left], nums[a]):
                                a += 1
                            while a < b and compare_big(nums[b], nums[left]):
                                b -= 1
                            if a < b and compare_big(nums[a], nums[b]):
                                nums[a], nums[b] = nums[b], nums[a]
                        if compare_big(nums[left], nums[a]):
                            nums[a], nums[left] = nums[left], nums[a]
                        elif compare_big(nums[left], nums[a - 1]):
                            nums[a - 1], nums[left] = nums[left], nums[a - 1]
                        x.append((left, a - 1))
                        x.append((a, right))

        nums = [str(i) for i in nums]
        quicksort(0, len(nums) - 1)
        r = ''
        for i in range(len(nums)-1, -1, -1):
            r += nums[i]
        if r[0] == '0':
            return '0'
        return r


print(Solution().largestNumber([1,2,2,2]))