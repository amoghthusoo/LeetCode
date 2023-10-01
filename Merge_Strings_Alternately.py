class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        outStr = ""

        try:
            i = 0
            while (i < len(word1)):

                outStr += word1[i] + word2[i]
                i += 1

            while (i < len(word2)):

                outStr += word2[i]
                i += 1
        except:

            while (i < len(word1)):

                outStr += word1[i]
                i += 1

        return outStr



word1 = "abcd"
word2 = "pq"
obj = Solution()
solution = obj.mergeAlternately(word1, word2)
print(solution)