class Solution:

    def max_digit(self, num):
        num = str(num)
        _max = num[0]
        
        for e in num:
            if(e > _max):
                _max = e
        
        return int(_max)     

    def maxSum(self, nums: list[int]) -> int:
        
        ans = -1

        i = 0 
        while(i < len(nums) - 1):

            j = i + 1
            while(j < len(nums)):

                if(self.max_digit(nums[i]) == self.max_digit(nums[j])):

                    temp_sum = nums[i] + nums[j]
                    if(temp_sum > ans):
                        ans = temp_sum

                j += 1
            i += 1
        
        return ans 

nums = [51,71,17,24,42]
obj = Solution()
result = obj.maxSum(nums)
print(result)
