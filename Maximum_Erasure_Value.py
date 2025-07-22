class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        
        ans = -1

        window = set()

        window_sum = 0
        i = 0
        j = 0
        while(j < len(nums)):

            if(nums[j] not in window):
                window.add(nums[j])
                window_sum += nums[j]
                if(window_sum > ans):
                    ans = window_sum
                j += 1
            
            else:

                while(nums[i] != nums[j]):

                    window.remove(nums[i])
                    window_sum -= nums[i]
                    i += 1
                
                window.remove(nums[i])
                window_sum -= nums[i]
                i += 1
        
        return ans

nums = [5,2,1,2,5,2,1,2,5]
obj = Solution()
result = obj.maximumUniqueSubarray(nums)
print(result)
