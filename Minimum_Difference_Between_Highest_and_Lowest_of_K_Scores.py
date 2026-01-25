class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        
        nums.sort()
        i = 0
        j = k - 1

        ans = nums[j] - nums[i]
        while(i <= len(nums) - k):
            
            diff = nums[j] - nums[i]
            if(diff < ans):
                ans = diff

            i += 1
            j += 1
        
        return ans

nums = [90]
k = 1
obj = Solution()
result = obj.minimumDifference(nums, k)
print(result)