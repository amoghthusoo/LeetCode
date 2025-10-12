from collections import Counter
class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        
        ans = []
        pattern_unique_len = len(Counter(pattern))
        for word in words:
            
            word_unique_len = len(Counter(word))

            if(word_unique_len != pattern_unique_len):
                continue

            map_dict = {}

            for i, ch in enumerate(pattern):
                if(ch not in map_dict):
                    map_dict[ch] = word[i]

            temp_word = ""
            for ch in pattern:
                temp_word += map_dict[ch]
            

            if(temp_word == word):
                ans.append(word)
        
        return ans

words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
obj = Solution()
result = obj.findAndReplacePattern(words, pattern)
print(result)
