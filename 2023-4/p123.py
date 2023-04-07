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

    def dp_plus(self, prices):
        n = len(prices)
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0
        for i in range(1, n):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        return sell2


print(Solution().maxProfit([1,2,4,2,5,7,2,4,9,0]))