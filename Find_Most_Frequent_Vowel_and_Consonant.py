from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        
        occr_dict = dict(Counter(s))

        vowel_freq = []
        consonant_freq = []

        for ch, freq in occr_dict.items():

            if(ch in ["a", "e", "i", "o", "u"]):
                vowel_freq.append(freq)
            else:
                consonant_freq.append(freq)
        
        vowel_max = 0
        consonant_max = 0

        try:
            vowel_max = max(vowel_freq)
        except:
            pass
        
        try:
            consonant_max = max(consonant_freq)
        except:
            pass

        return vowel_max + consonant_max