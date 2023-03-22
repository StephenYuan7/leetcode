'''
题解用的回溯法，想提速得剪枝
按序遍历dict for key in sorted(dict)
list.append(x)不返回值
双重列表去重 list(set(tuple(sorted(sub)) for sub in r))
'''
class Solution:
    def combinationSum(self, candidates, target: int):
        candidates = sorted(candidates)
        a = {}
        r = []
        for i in candidates:
            if i < target:
                a[i] = [[i]]
            elif i == target:
                r.append([i])
        for i in range(target//candidates[0]):
            b = {}
            for j in candidates:
                for k in sorted(a):
                    if j + k == target:
                        for x in a[k]:
                            r.append([j] + x)
                    elif j + k < target:
                        if (j + k) not in b:
                            b[j + k] = []
                        for x in a[k]:
                            b[j + k].append([j] + x)
                    else:
                        break
            a = b.copy()
        return list(set(tuple(sorted(sub)) for sub in r))


print(Solution().combinationSum([2,3,7], 18))
