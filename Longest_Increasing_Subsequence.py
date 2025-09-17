class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        
        dp = [1 for _ in range(len(nums))]

        i = 0
        while(i < len(dp)):

            j = 0
            while(j < i):

                if(nums[i] > nums[j]):
                    dp[i] = max(dp[i], dp[j] + 1)

                j += 1
            i += 1

        return max(dp)
    
nums = [7,7,7,7,7,7,7]
obj = Solution()
result = obj.lengthOfLIS(nums)
print(result)