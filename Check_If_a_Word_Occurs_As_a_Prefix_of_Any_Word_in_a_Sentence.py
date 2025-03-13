class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        sentence = sentence.split()

        for i, word in enumerate(sentence):

            if(word.find(searchWord) == 0):
                return i + 1
        
        return -1
    
sentence = "i love eating burger"
searchWord = "burg"
obj = Solution()
out = obj.isPrefixOfWord(sentence, searchWord)
print(out)