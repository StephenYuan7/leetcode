class Solution:
    def longestConsecutive(self, nums) -> int:
        x = {i: 1 for i in nums}
        r = 0
        for i in x:
            if x[i] == 1:
                a = i + 1
                b = i - 1
                while a in x and x[a] == 1:
                    x[a] = 0
                    a += 1

                while b in x and x[b] == 1:
                    x[b] = 0
                    b -= 1

                r = max(a - b - 1, r)
        return r


print(Solution().longestConsecutive([100,4,200,1,3,2]))