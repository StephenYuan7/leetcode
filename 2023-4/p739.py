'''
题解用了堆栈，速度更快
'''
class Solution:
    def dailyTemperatures(self, temperatures):
        a = {}
        b = []
        r = [0] * len(temperatures)
        for i, temperature in enumerate(temperatures):
            t = 0
            for j in b:
                if j in a:
                    if j < temperature:
                        for k in a[j]:
                            r[k] = i - k
                        t += 1
                        del a[j]
                    else:
                        break
            if t == len(b):
                b = [temperature]
            else:
                b = b[t:]
                if temperature < b[0]:
                    b.insert(0, temperature)
            if temperature in a:
                a[temperature].append(i)
            else:
                a[temperature] = [i]
        return r

    def dailyTemperatures_plus(self, temperatures):
        length = len(temperatures)
        ans = [0] * length
        stack = []
        for i in range(length):
            temperature = temperatures[i]
            while stack and temperature > temperatures[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans



print(Solution().dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))