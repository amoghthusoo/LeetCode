class Solution:
    def arrayStringsAreEqual(self, word1: list, word2: list) -> bool:
        
        def listToStr(l) -> str:

            s = ""
            for e in l:
                s += e

            return s

        if (listToStr(word1) == listToStr(word2)):
            return True
        else:
            return False

word1  = ["abc", "d", "defg"]
word2 = ["abcddefg"]
obj = Solution()
solution = obj.arrayStringsAreEqual(word1, word2)
print(solution)