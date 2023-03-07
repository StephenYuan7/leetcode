class Solution:
    def numberOfWeakCharacters(properties) -> int:
        properties.sort(key=lambda i: i[0], reverse=True)
        max = {}
        x = properties[0][0]
        x_max = 0
        for i in properties:
            if i[0] < x:
                max[i[0]] = x_max
                x = i[0]
            if i[1] > x_max:
                x_max = i[1]
        max[properties[0][0]] = 0
        r = 0
        for i in properties:
            if i[1] < max[i[0]]:
                r += 1
        return r


test = [[2,2],[3,3]]
Solution.numberOfWeakCharacters(test)
