class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2[::-1], num1[::-1]
        else:
            num1, num2 = num1[::-1], num2[::-1]

        res = ''
        a = 0
        for i in range(len(num2)):
            t = int(num1[i]) + int(num2[i]) + a
            if t >= 10:
                a = 1
                t -= 10
            else:
                a = 0
            res += str(t)
        for i in range(len(num2), len(num1)):
            t = int(num1[i]) + a
            if t >= 10:
                a = 1
                t -= 10
            else:
                a = 0
            res += str(t)
        if a == 1:
            res += '1'
        return res[::-1]


print(Solution().addStrings('9', '99'))