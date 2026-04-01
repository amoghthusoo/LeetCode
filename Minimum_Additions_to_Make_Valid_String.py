class Solution:
    def addMinimum(self, word: str) -> int:

        word = word.replace("abc", "0")
        word = word.replace("ab", "1")
        word = word.replace("bc", "1")
        word = word.replace("ac", "1")
        word = word.replace("a", "2")
        word = word.replace("b", "2")
        word = word.replace("c", "2")

        ans = 0
        for e in word:
            ans += int(e)
        
        return ans