from collections import Counter
class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        
        return [words[0]] + [words[i] for i in range(1, len(words)) if Counter(words[i]) != Counter(words[i - 1])]
    
    
words = ["a","b","c","d","e"]
obj = Solution()
result = obj.removeAnagrams(words)
print(result)