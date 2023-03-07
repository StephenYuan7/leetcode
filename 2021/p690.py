class Solution:
    def getImportance(self, employees: list, id: int) -> int:
        new = {id}
        exist = set()
        new.difference_update(exist)
        while new:
            exist = exist.union(new)
            x = set()
            for i in new:
                for j in employees:
                    if j[0] == i:
                        y = j
                        break
                for j in y[2]:
                    x.add(j)
            x.difference_update(exist)
            new = x
        r = 0
        for i in exist:
            for j in employees:
                if j[0] == i:
                    y = j
                    break
            r += y[1]
        return r


s = Solution()
print(s.getImportance([[2, 5, []]], 2))
