from collections import Counter
class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        occr_dict = Counter(nums)
        if(occr_dict[nums[len(nums)//2]] == 1):
            return True
        
        return False

nums = [1,2,3]
obj = Solution()
result = obj.isMiddleElementUnique(nums)
print(result)