class Solution:
    def removeDuplicates(self, nums) -> int:
        a = 0
        for i in range(len(nums)-1):
            if nums[i+1] != nums[i]:
                a += 1
                nums[a] = nums[i+1]
        return a+1


print(Solution().removeDuplicates([1,1,2]))
