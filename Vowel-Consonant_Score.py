class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        
        vowels = {"a", "e", "i", "o", "u"}
        v = c = 0
        for ch in s:
            if(ch in vowels):
                v += 1
            elif(ch.isalpha()):
                c += 1
        
        return v // c if (c > 0) else 0