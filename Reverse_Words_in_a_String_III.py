class Solution:
    def reverseWords(self, s: str) -> str:
        
        def reverseWord(word):

            reversedWord = ""

            i = len(word) - 1

            while (i >= 0):
                reversedWord += word[i]
                i -= 1

            return reversedWord

        ansList = s.split()

        i = 0
        while (i < len(ansList)):

            ansList[i] = reverseWord(ansList[i])
            i += 1

        ansStr = ""

        i = 0
        while (i < len(ansList)):
            
            ansStr += ansList[i]

            if (i != len(ansList) - 1):
                ansStr += " "
            
            
            i += 1

        return ansStr

s = "Let's take LeetCode contest"
obj = Solution()
solution = obj.reverseWords(s)
print(solution)