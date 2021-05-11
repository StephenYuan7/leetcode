class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        x1 = len(nums1)
        x2 = len(nums2)
        l = x1 + x2
        count = 0
        a = 0
        b = 0
        if x1 == 0:
            if l % 2:
                return nums2[l // 2]
            else:
                return (nums2[l // 2] + nums2[l // 2 - 1]) / 2
        if x2 == 0:

            if l % 2:
                return nums1[l // 2]
            else:
                return (nums1[l // 2] + nums1[l // 2 - 1]) / 2
        if l % 2:
            for i in range(l // 2 + 1):
                if b >= x2:
                    x = nums1[a]
                    a += 1
                elif a >= x1 or nums1[a] > nums2[b]:
                    x = nums2[b]
                    b += 1
                else:
                    x = nums1[a]
                    a += 1
            return x
        else:
            for i in range(l // 2):
                if b >= x2:
                    x = nums1[a]
                    a += 1
                elif a >= x1 or nums1[a] > nums2[b]:
                    x = nums2[b]
                    b += 1
                else:
                    x = nums1[a]
                    a += 1
            if b >= x2:
                return (x + nums1[a]) / 2
            if a >= x1 or nums1[a] > nums2[b]:
                return (x + nums2[b]) / 2
            else:
                return (x + nums1[a]) / 2

m = Solution()
l1 = [2, 3]
l2 = [1]
p = m.findMedianSortedArrays(l1, l2)
print(p)
