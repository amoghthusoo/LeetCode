from itertools import combinations
from sortedcontainers import SortedDict
from collections import Counter

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        
        intr_dict = dict()

        i = 0
        while(i <= len(nums)):

            combs = combinations(nums, i)

            for comb in combs:
                occr_dict = str(SortedDict(Counter(comb)))

                if(occr_dict not in intr_dict):
                    intr_dict[occr_dict] = list(comb)

            i += 1
        
        ans = []
        for key, val in intr_dict.items():
            ans.append(val)
        
        return ans

nums = [1, 2, 2]
obj = Solution()
result = obj.subsetsWithDup(nums)
print(result)
