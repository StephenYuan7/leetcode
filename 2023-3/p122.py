class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = 0
        min_price = prices[0]
        for price in prices:
            if price > min_price:
                r += price - min_price
            min_price = price
        return r
