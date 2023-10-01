class Solution:
    def mostWordsFound(self, sentences: list) -> int:
        
        return max([len(sentence.split()) for sentence in sentences])

sentences = ["please wait", "continue to fight", "continue to win"]
obj = Solution()
solution = obj.mostWordsFound(sentences)
print(solution)