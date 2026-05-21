from collections import Counter
from sortedcontainers import SortedDict

class Solution:
    def sortString(self, s: str) -> str:
        
        freq_dict = Counter(s)
        freq_dict = SortedDict(freq_dict)


        ans = ""

        flag = True
        while(flag):

            flag = False

            for ch, freq in freq_dict.items():

                if(freq != 0):
                    ans += ch
                    freq_dict[ch] -= 1
                    flag = True
            
            for ch, freq in reversed(list(freq_dict.items())):
                
                if(freq != 0):
                    ans += ch
                    freq_dict[ch] -= 1
                    flag = True

        return ans

s = "rat"
obj = Solution()
result = obj.sortString(s)
print(result)