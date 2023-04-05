class Solution:
    def findMedianSortedArrays_failed(self, nums1, nums2) -> float:
        nums1_left = 0
        nums2_left = 0
        num1_left_t = nums1_left
        num2_left_t = nums2_left
        t = 0
        while nums1_left < len(nums1) and nums2_left < len(nums2) and t < (len(nums1) + len(nums2)) // 2 - 1:
            num1_left_t = nums1_left
            num2_left_t = nums2_left
            nums1_middle = (nums1_left + len(nums1) - 1) // 2
            nums2_middle = (len(nums2) - 1 + nums2_left) // 2
            if nums1[nums1_middle] > nums2[nums2_middle]:
                t += max(nums2_middle - nums2_left, 1)
                nums2_left = nums2_middle
            else:
                t += max(nums1_middle - nums1_left, 1)
                nums1_left = nums1_middle
        if num1_left_t > 0:
            num1_left_t -= 1
        if num2_left_t > 0:
            num2_left_t -= 1
        t = num2_left_t + num1_left_t
        while t <= (len(nums1) + len(nums2)) // 2 + 1:
            t += 1
            if num1_left_t < len(nums1):
                if num2_left_t < len(nums2):
                    if nums1[num1_left_t] < nums2[num2_left_t]:
                        num1_left_t += 1
                    else:
                        num2_left_t += 1
                else:
                    num1_left_t += 1
            else:
                num2_left_t += 1
        if (len(nums1) + len(nums2)) % 2 == 0:
            if num1_left_t < len(nums1):
                if num2_left_t < len(nums2):
                    if nums1[num1_left_t] < nums2[num2_left_t]:
                        if num1_left_t == len(nums1) - 1:
                            return (nums1[num1_left_t] + nums2[num2_left_t]) / 2
                        else:
                            return (nums1[num1_left_t] + min(nums1[num1_left_t + 1], nums2[num2_left_t])) / 2
                    else:
                        if num2_left_t == len(nums2) - 1:
                            return (nums1[num1_left_t] + nums2[num2_left_t]) / 2
                        else:
                            return (nums2[num2_left_t] + min(nums2[num2_left_t + 1], nums1[num1_left_t])) / 2
                else:
                    return (nums1[num1_left_t] + nums1[num1_left_t + 1]) / 2
            else:
                return (nums2[num2_left_t] + nums2[num2_left_t + 1]) / 2
        else:
            if num1_left_t < len(nums1):
                if num2_left_t < len(nums2):
                    return min(nums1[num1_left_t], nums2[num2_left_t])
                else:
                    return nums1[num1_left_t]
            else:
                return nums2[num2_left_t]

    def findMedianSortedArrays(self, nums1, nums2):
        def find_k(nums1, nums2, start1, start2, end1, end2, k):
            len1 = end1 - start1 + 1
            len2 = end2 - start2 + 1
            if len1 > len2:
                return find_k(nums2, nums1, start2, start1, end2, end1, k)
            if len1 == 0:
                return nums2[start2 + k - 1]
            if k == 1:
                return min(nums1[start1], nums2[start2])
            i = start1 + min(len1, k // 2) - 1
            j = start2 + min(len2, k // 2) - 1
            if nums1[i] > nums2[j]:
                return find_k(nums1, nums2, start1, j + 1, end1, end2, k - (j - start2 + 1))
            else:
                return find_k(nums1, nums2, i + 1, start2, end1, end2, k - (i - start1 + 1))

        return (find_k(nums1, nums2, 0, 0, len(nums1) - 1, len(nums2) - 1, (len(nums1) + len(nums2) + 1) // 2) +
                find_k(nums1, nums2, 0, 0, len(nums1) - 1, len(nums2) - 1, (len(nums1) + len(nums2) + 2) // 2)) / 2


print(Solution().findMedianSortedArrays([1, 3], [2]))
