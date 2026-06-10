from collections import Counter
class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        
        occr_dict = Counter(nums)
        ans = []

        for num, freq in occr_dict.items():
            if(freq <= k):
                ans.extend([num] * freq)
            else:
                ans.extend([num] * k)
        
        return ans

nums = [1,1,1,2,2,3]
k = 2
obj = Solution()
result = obj.limitOccurrences(nums, k)
print(result)