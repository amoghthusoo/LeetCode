class Solution:
    def stringMatching(self, words: list) -> list:
        
        ansList = []

        i = 0
        while (i < len(words)):

            j = 0
            while (j < len(words)):

                if ((j != i) and (words[i] in words[j])):
                    ansList.append(words[i])
                    break

                j += 1

            i += 1

        return ansList

words = ["blue","green","bu"]
obj = Solution()
solution = obj.stringMatching(words)
print(solution)