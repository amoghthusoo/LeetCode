class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        
        ans = 0
        zero_arr_mem = False
        count = 0
        i = 0
        while(i < len(nums)):

            if(nums[i] == 0):
                if(not zero_arr_mem):
                    zero_arr_mem = True
                count += 1

            elif(zero_arr_mem):
                zero_arr_mem = False
                ans += (count * (count + 1)) // 2
                count = 0
            
            i += 1

        if(count != 0):
            ans += (count * (count + 1)) // 2

        return ans

nums = [1,3,0,0,2,0,0,4]
obj = Solution()
result = obj.zeroFilledSubarray(nums)
print(result)
