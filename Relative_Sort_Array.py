from collections import Counter
from sortedcontainers import SortedDict

class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:

        ans = []        
        freq_dict = Counter(arr1)

        for e in arr2:
            ans.extend([e] * freq_dict[e])
            freq_dict.pop(e)

        freq_dict = SortedDict(freq_dict)
        
        for e, f in freq_dict.items():
            ans.extend([e] * f)
        
        return ans
    
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
obj = Solution()
result = obj.relativeSortArray(arr1, arr2)
print(result)