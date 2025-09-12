class Solution:
    def doesAliceWin(self, s: str) -> bool:
        
        vowel_count = 0

        for ch in s:
            if(ch in ["a", "e", "i", "o", "u"]):
                vowel_count += 1
        
        if(vowel_count == 0):
            return False
        else:
            return True