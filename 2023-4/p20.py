'''
简单的堆栈
'''
class Solution:
    def isValid(self, s: str):
        r = ''
        for i in s:
            if i in '({[':
                r += i
            elif r == '':
                return False
            elif i == ')':
                if r[-1] != '(':
                    return False
                r = r[:-1]
            elif i == '}':
                if r[-1] != '{':
                    return False
                r = r[:-1]
            else:
                if r[-1] != '[':
                    return False
                r = r[:-1]
        if r:
            return False
        return True


print(Solution().isValid("()"))