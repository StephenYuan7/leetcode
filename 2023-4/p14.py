class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def longestCommon(strs, index):
            for s in strs:
                if index >= len(s) or s[index] != strs[0][index]:
                    return False
            return True

        r = 0
        for i in range(len(strs[0])):
            if longestCommon(strs, i):
                r += 1
            else:
                break
        return strs[0][:r]
