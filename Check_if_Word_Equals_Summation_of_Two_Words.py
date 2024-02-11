class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
        alphabets = [chr(i) for i in range(97, 123)]
        values = [str(i) for i in range(26)]
        encryptionDict = dict(zip(alphabets, values))

        def wordToNum(word : str) -> int:
            
            intStr = ""

            for ch in word:
                intStr += encryptionDict[ch]

            return int(intStr)

        if (wordToNum(firstWord) + wordToNum(secondWord) == wordToNum(targetWord)):
            return True
        else:
            return False

firstWord = "aaa"
secondWord = "a"
targetWord = "aaaa"
obj = Solution()
solution = obj.isSumEqual(firstWord, secondWord, targetWord)
print(solution)