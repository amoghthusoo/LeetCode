from collections import Counter
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        
        if(len(word) < 5):
            return 0
        
        count = 0
        for i in range(len(word) - 4):
            for j in range(i + 5, len(word) + 1):
                occr_dict = dict(Counter(word[i : j]))
                if("a" in occr_dict and
                   "e" in occr_dict and
                   "i" in occr_dict and
                   "o" in occr_dict and
                   "u" in occr_dict and
                   len(occr_dict.keys()) == 5):
                    count += 1
                
        return count
    
s = "cuaieuouac"
# print(len(s))
obj = Solution()
print("start")
out = obj.countVowelSubstrings(s)
print("end")
print(out)