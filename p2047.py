class Solution:
    def countValidWords(self, sentence: str) -> int:
        s = sentence.split()
        r = 0
        for word in s:
            count_ = 0
            t = 1
            for index, i in enumerate(word):
                if '0'<= i <='9':
                    t = 0
                    break
                if i == '-':
                    if count_ == 0:
                        count_ = 1
                        if index == 0 or index == len(word)-1 or word[index - 1] < 'a' or word[index - 1] > 'z' or word[
                            index + 1] < 'a' or word[index + 1] > 'z':
                            t = 0
                            break
                    else:
                        t = 0
                        break
                if (i == '!' or i == '.' or i == ',') and index != len(word)-1:
                    t = 0
                    break
            if t:
                r += 1
        return r
