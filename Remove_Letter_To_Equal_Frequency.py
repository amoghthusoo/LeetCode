from collections import Counter
from copy import deepcopy

class Solution:

    def hasEqualFrequency(self, s):
        
        occ_dict = dict(Counter(s))

        reference_occ = occ_dict[s[0]]

        for key, val in occ_dict.items():
            if(val != reference_occ):
                return False
            
        return True

    def equalFrequency(self, word: str) -> bool:
        
        word = list(word)

        i = 0
        while(i < len(word)):
            
            temp = deepcopy(word)
            temp.pop(i)

            if(self.hasEqualFrequency(temp)):
                return True
            
            i += 1

        return False
    
word = "aazz"
obj = Solution()
out = obj.equalFrequency(word)
print(out)