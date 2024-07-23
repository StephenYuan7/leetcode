class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = []
        r = s[0]
        for i in range(len(s)):
            t = []
            for j in left:
                if j - 1 > -1 and s[j - 1] == s[i]:
                    t.append(j - 1)
            if i - 1 > -1 and s[i - 1] == s[i]:
                t.append(i - 1)
            t.append(i)
            if i - t[0] + 1 > len(r):
                r = s[t[0]: i + 1]
            left = t
        return r


print(Solution().longestPalindrome("babad"))