class Solution:

    def __init__(self):
        self.vowels = {"a", "e", "i", "o", "u"} 

    def count_vowels(self, word):
        cnt = 0

        for ch in word:
            if(ch in self.vowels):
                cnt += 1

        return cnt


    def reverseWords(self, s: str) -> str:
        
        

        words = s.split()
        cnt = self.count_vowels(words[0])
        
        i = 1
        while(i < len(words)):

            if(self.count_vowels(words[i]) == cnt):
                words[i] = words[i][-1::-1]

            i += 1  
        
        return " ".join(words)

s = "book is nice"
obj = Solution()
result = obj.reverseWords(s)
print(result)