'''
原思路，取出每天最前的最低点和每天之后的最高点，遍历两次
题解的意思是每天减去最低点即可
'''
class Solution:
    def maxProfit(self, prices) -> int:
        min_price = prices.copy()
        max_price = prices.copy()
        min_p = prices[0]
        for i in range(len(prices)):
            min_p = min(min_p, prices[i])
            min_price[i] = min_p
        max_p = prices[-1]
        for i in range(len(prices)):
            max_p = max(max_p, prices[len(prices) - 1 - i])
            max_price[len(prices) - 1 - i] = max_p
        t = prices.copy()
        for i in range(len(prices)):
            t[i] = max_price[i] - min_price[i]
        t.append(0)
        return max(t)

    def solution(self, prices):
        minprice = int(1e9)
        maxprofit = 0
        for price in prices:
            if price - minprice > maxprofit:
                maxprofit = price - minprice
            else:
                minprice = min(price, minprice)
        return maxprofit


prices = [7,1,5,3,6,4]
Solution().maxProfit(prices)