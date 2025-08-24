class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        
        zero_count = 0
        max_window = -1

        i = 0
        j = 0
        while(j < len(nums)):

            if(nums[j] == 0):
                zero_count += 1

            while(zero_count >= 2):

                if(nums[i] == 0):
                    zero_count -= 1
                
                i += 1

            if(j - i + 1 > max_window):
                max_window = j - i + 1
            
            j += 1

        return max_window - 1

nums = [1,1,1]
obj = Solution()
result = obj.longestSubarray(nums)
print(result)            