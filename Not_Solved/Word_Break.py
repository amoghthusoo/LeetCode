# NOT SOLVED
class Solution:
    def wordBreak(self, s: str, wordDict: list) -> bool:

        s = list(s)
        wordDictList = []
        for word in wordDict:
            wordDictList.append(list(word))
        

        for word in wordDictList:

            for letter in word:

                try:
                    s.pop(s.index(letter))
                except:
                    return False
                
        return True

     

s = "applepenapple"
wordDict = ["leet","code"]
obj = Solution()
solution = obj.wordBreak(s, wordDict)
print(solution)
