def p213(nums):
    l = len(nums)
    if l == 1:
        return nums[0]
    if l == 2 or l == 3:
        return max(nums)
    if l % 2:
        x1 = nums[1::2]
        for i in range(0,l//2-1):
            pass
        x2 = nums[:-1:2]
        x3 = nums[0::2]
    else:
        x1 = nums[1::2]
        x2 = nums[::2]
    return max(sum(x1), sum(x2), sum(x3))


nums = [2, 3, 2, 1, 1, 1]
print(p213(nums))
