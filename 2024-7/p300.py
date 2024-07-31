class Solution:
    def lengthOfLIS(self, nums):
        r = [nums[0]]
        for i in nums:
            r[0] = min(r[0], i)
            for j in range(len(r)):
                if i > r[j]:
                    if j + 1 >= len(r):
                        r.append(i)
                    else:
                        r[j + 1] = min(r[j + 1],  i)
        return len(r)

print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))