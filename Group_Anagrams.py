from collections import Counter
from sortedcontainers import SortedDict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        group_dict = {}

        for s in strs:

            occr_dict = str(SortedDict(Counter(s)))

            if(occr_dict not in group_dict):
                group_dict[occr_dict] = [s]
            else:
                group_dict[occr_dict].append(s)
        
        ans = []
        for key, val in group_dict.items():
            ans.append(val)
        
        return ans
             
strs = ["eat","tea","tan","ate","nat","bat"]
obj = Solution()
result = obj.groupAnagrams(strs)
print(result)
