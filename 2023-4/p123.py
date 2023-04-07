'''
动态规划
'''
class Solution:
    def maxProfit(self, prices) -> int:
        left = [0] * len(prices)
        right = [0] * len(prices)
        left_min = prices[0]
        for i in range(len(prices)):
            left[i] = prices[i] - left_min
            left_min = min(left_min, prices[i])
        for i in range(len(prices) - 1):
            left[i + 1] = max(left[i], left[i + 1])
        right_max = prices[-1]
        for i in range(len(prices) - 1, -1, -1):
            right[i] = right_max - prices[i]
            right_max = max(prices[i], right_max)
        r = 0
        for i in range(len(prices)):
            r = max(r, left[i] + right[i])
        return r



print(Solution().maxProfit([1,2,4,2,5,7,2,4,9,0]))