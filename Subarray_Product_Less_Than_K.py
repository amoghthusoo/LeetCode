class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        
        i = 0
        j = -1
        ans = 0
        window_product = 1
        while(True):
            
            j += 1

            if(j >= len(nums)):
                break

            window_product *= nums[j]

            if(window_product < k):
                ans += (j - i + 1)
            
            else:

                while(window_product >= k and i <= j):

                    window_product //= nums[i]
                    i += 1
                
                ans += (j - i + 1)
        
        return ans
    
nums = [1,2,3]
k = 0
obj = Solution()
result = obj.numSubarrayProductLessThanK(nums, k)
print(result)