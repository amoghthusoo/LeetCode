class Solution:

    def is_increasing(self, arr):

        for i in range(len(arr) - 1):

            if(arr[i] >= arr[i + 1]):
                return False
        
        return True
    
    def is_decreasing(self, arr):

        for i in range(len(arr) - 1):

            if(arr[i] <= arr[i + 1]):
                return False
        
        return True

    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        
        max_len = -1
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                
                sub_arr = nums[i : j + 1]
                if(self.is_increasing(sub_arr) or self.is_decreasing(sub_arr)):

                    curr_len = j - i + 1
                    if(curr_len > max_len):
                        max_len = curr_len
        
        return max_len

nums = [1,4,3,3,2]
obj = Solution()
result = obj.longestMonotonicSubarray(nums)
print(result)