class Solution:
    def countValidWords(self, sentence: str) -> int:
        r = 0
        for word in sentence.split():
            if self.valid(word):
                r += 1
        return r

    def valid(self, word):
        count_ = 0
        for index, i in enumerate(word):
            if i.isdigit():
                return False
            if i == '-':
                if count_ == 0:
                    if index == 0 or index == len(word) - 1 or not word[index - 1].islower() \
                            or not word[index + 1].islower():
                        return False
                    count_ = 1
                else:
                    return False
            if (i == '!' or i == '.' or i == ',') and index != len(word) - 1:
                return False
        return True
