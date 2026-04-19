class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        
        occr_dict = {}
        max_window_size = -1
        i = j = 0
        while(j < len(nums)):

            if(nums[j] not in occr_dict):
                occr_dict[nums[j]] = 1
                # j += 1
            else:

                if(occr_dict[nums[j]] < k):
                    occr_dict[nums[j]] += 1
                    # j += 1
                
                else:
                    window_size = j - i
                    if(window_size > max_window_size):
                        max_window_size = window_size
                    
                    while(nums[i] != nums[j]):
                        occr_dict[nums[i]] -= 1
                        i += 1
                    i += 1
            j += 1

        window_size = j - i
        if(window_size > max_window_size):
            max_window_size = window_size

        return max_window_size
    
nums = [1,2,3,1,2,3,1,2]
k = 2
obj = Solution()
result = obj.maxSubarrayLength(nums, k)
print(result)
                    