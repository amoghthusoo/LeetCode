class Solution:

    def isPrefixAndSuffix(self, str1 : str, str2 : str):

        if(str2.find(str1) == 0 and str2[-1 : : -1].find(str1[-1 : : -1]) == 0):
            return True
         
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        
        count = 0

        i = 0
        while(i < len(words)):
            
            j = i + 1
            while(j < len(words)):

                if(self.isPrefixAndSuffix(words[i], words[j])):
                    count += 1

                j += 1
            i += 1

        return count