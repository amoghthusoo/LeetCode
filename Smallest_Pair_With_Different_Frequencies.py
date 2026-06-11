from collections import Counter
class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        
        intr_ans = []
        occr_dict = Counter(nums)
        keys = sorted(list(occr_dict.keys()))

        i = 0
        while(i < len(keys)):

            j = i + 1
            while(j < len(keys)):

                if(occr_dict[keys[i]] != occr_dict[keys[j]]):
                    intr_ans.append([keys[i], keys[j]])

                j += 1
            i += 1
        
        intr_ans.sort()

        return intr_ans[0] if intr_ans else [-1, -1]

nums = [5,5,4]
obj = Solution()
result = obj.minDistinctFreqPair(nums)
print(result)