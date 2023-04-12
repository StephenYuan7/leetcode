class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = 0
        a = {}
        for i in range(len(s)):
            if s[i] in a:
                a = {key: value for key, value in a.items() if value > a[s[i]]}
            a[s[i]] = i
            r = max(r, len(a))
        return r


print(Solution().lengthOfLongestSubstring('abcabcbb'))
