'''
快排可以从递归改成堆栈，取数可以随机，对特殊情况可以进行单独考虑
'''
class Solution:
    def sortArray(self, nums):
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
                            while a < b and nums[a] <= nums[left]:
                                a += 1
                            while a < b and nums[b] > nums[left]:
                                b -= 1
                            if a < b and nums[a] > nums[b]:
                                nums[a], nums[b] = nums[b], nums[a]
                        if nums[a] < nums[left]:
                            nums[a], nums[left] = nums[left], nums[a]
                        elif nums[a - 1] < nums[left]:
                            nums[a - 1], nums[left] = nums[left], nums[a - 1]
                        x.append((left, a - 1))
                        x.append((a, right))

        quicksort(0, len(nums) - 1)
        return nums


print(Solution().sortArray([2, 2, 2, 2, 2, 2, 2, 2]))