class Solution:
    def maximumNumberOfStringPairs(self, words: list) -> int:
        
        def reverseStr(s):

            reversed = ""

            i = len(s) - 1
            while (i >= 0):
                reversed += s[i]
                i -= 1

            return reversed
        
        count = 0
        i = 0
        while (i < len(words)):
            
            j = i + 1
            while (j < len(words)):

                if (words[i] == reverseStr(words[j])):
                    count += 1

                j += 1
            
            i += 1

        return count

words = ["aa","ab"]
obj = Solution()
solution = obj.maximumNumberOfStringPairs(words)
print(solution)