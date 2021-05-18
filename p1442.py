class Solution:
    def countTriplets(self, arr: list[int]) -> int:
        x = [0] * len(arr)
        x[0] = arr[0]
        r = 0
        for i in range(1, len(arr)):
            x[i] = x[i - 1] ^ arr[i]
            if x[i] == 0:
                r += i
        for i in range(1, len(arr)):
            for j in range(i, len(arr)):
                if x[i - 1] ^ x[j] == 0:
                    r += j - i
        return r
