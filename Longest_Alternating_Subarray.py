class Solution:
    def alternatingSubarray(self, nums: list[int]) -> int:

        def is_alternating(arr):

            i = 0
            while(i < len(arr) - 1):

                if(i % 2 == 0):
                    
                    if(arr[i + 1] - arr[i] != 1):
                        return False
                
                else:

                    if(arr[i + 1] - arr[i] != -1):
                        return False

                i += 1
            
            return True
        
        ans = -1
        i = 0
        while(i < len(nums)):

            temp = [nums[i]]
            j = i + 1
            while(j < len(nums)):
                
                temp.append(nums[j])
                if(is_alternating(temp)):
                    ans = max(ans, j - i + 1)

                j += 1
            i += 1
        
        return ans

nums = [2,3,4,3,4]
obj = Solution()
result = obj.alternatingSubarray(nums)
print(result)