from itertools import accumulate
class Solution:
    def dominantIndices(self, nums: list[int]) -> int:
        
        acc = list(reversed(list(accumulate(reversed(nums)))))
        ans = 0
        i = 0
        while(i < len(nums) - 1):

            if(nums[i] > acc[i + 1]/(len(nums) - i - 1)):
                ans += 1

            i += 1
        
        return ans 

nums = [5,4,3]
obj = Solution()
result = obj.dominantIndices(nums)
print(result)
