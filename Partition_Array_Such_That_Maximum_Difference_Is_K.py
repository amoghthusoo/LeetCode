class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        
        nums.sort()

        ans = 0
        min_e = nums[0]
        for i, e in enumerate(nums):

            if(e - min_e > k):
                min_e = e
                ans += 1
        
        ans += 1
        
        return ans
    
nums = [3,6,1,2,5]
k = 2
obj = Solution()
result = obj.partitionArray(nums, k)
print(result)