from collections import Counter;

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        
        occrDict1 = dict(Counter(word1))
        occrDict2 = dict(Counter(word2))


        for letter, occurrence in occrDict1.items():

            freq1 = occurrence

            if(letter in occrDict2):
                freq2 = occrDict2[letter]
            else:
                freq2 = 0

            if(abs(freq1 - freq2) > 3):
                return False
        
        for letter, occurrence in occrDict2.items():

            freq1 = occurrence

            if(letter in occrDict1):
                freq2 = occrDict1[letter]
            else:
                freq2 = 0

            if(abs(freq1 - freq2) > 3):
                return False

        return True
    
word1 = "cccddabba"
word2 = "babababab"
obj = Solution()
out = obj.checkAlmostEquivalent(word1, word2)
print(out)