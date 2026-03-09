class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        lower = upper = 0

        for ch in word:
            if(ch.islower()):
                lower += 1
            else:
                upper += 1
        
        if(upper == 0 or lower == 0 or (upper == 1 and lower == len(word) - 1 and word[0].isupper())):
            return True
        
        return False