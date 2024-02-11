class Solution:
    def findWords(self, words: list) -> list:
        
        def ofOnlyGivenRow(word, row):

            for letter in word:

                if (letter not in row):
                    return False
    
            return True

        rowDict = {"row1" : "qwertyuiopQWERTYUIOP",
                   "row2" : "asdfghjklASDFGHJKL",
                   "row3" : "zxcvbnmZXCVBNM"}
        

        ansList = []

        for word in words:

            if (
                ofOnlyGivenRow(word, rowDict["row1"]) or
                ofOnlyGivenRow(word, rowDict["row2"]) or
                ofOnlyGivenRow(word, rowDict["row3"])
                ):

                ansList.append(word)

        return ansList


words = ["adsdf","sfd"]
obj = Solution()
solution = obj.findWords(words)
print(solution)
