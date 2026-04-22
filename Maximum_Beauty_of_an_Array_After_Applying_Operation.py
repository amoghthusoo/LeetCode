class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        
        nums.sort()

        max_len = 0
        i = j = 0
        while(j < len(nums)):

            if(nums[j] - nums[i] <= k * 2):
                curr_len = j - i + 1
                if(curr_len > max_len):
                    max_len = curr_len
                
                j += 1
            
            else:

                while(nums[j] - nums[i] > k * 2):
                    i += 1
            
        return max_len

nums = [1,1,1,1]
k = 10
obj = Solution()
result = obj.maximumBeauty(nums, k)
print(result)