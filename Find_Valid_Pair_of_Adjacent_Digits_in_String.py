from collections import Counter

class Solution:
    def findValidPair(self, s: str) -> str:

        freq_dict = Counter(s)

        i = 0
        while(i < len(s) - 1):

            if(s[i] != s[i + 1] and freq_dict[s[i]] == int(s[i]) and freq_dict[s[i + 1]] == int(s[i + 1])):
                return s[i] + s[i + 1]

            i += 1        

        return ""