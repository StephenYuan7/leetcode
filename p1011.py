class Solution:
    def shipWithinDays(self, weights: list[int], D: int) -> int:
        minx = max(weights)
        maxx = 500
        while minx != maxx:
            x = (minx + maxx) // 2
            d = 1
            w = 0
            for i in weights:
                w += i
                if w > x:
                    d += 1
                    w = i
            if d > D:
                minx = x + 1
            else:
                maxx = x
        return minx


s = Solution()
print(s.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
