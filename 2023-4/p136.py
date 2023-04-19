'''
可以用哈希表，但题解用的异或
'''
from functools import reduce


class Solution:
    def singleNumber(self, nums):
        return reduce(lambda x, y: x ^ y, nums)