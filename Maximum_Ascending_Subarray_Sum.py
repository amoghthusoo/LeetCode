class Solution:
    def maxAscendingSum(self, nums:list[int]) -> int:
        
        maxSum = -1
        interSum = 0

        i = 0
        while(i < len(nums)):

            if(i == 0):
                interSum += nums[i]

            else:

                if(nums[i] > nums[i - 1]):
                    interSum += nums[i]
                
                else:

                    if(interSum > maxSum):
                        maxSum = interSum

                    interSum = 0
                    interSum += nums[i]

            i += 1

        if(interSum > maxSum):
            maxSum = interSum

        return maxSum



nums = [12,17,15,13,10,11,12]
obj = Solution()
out = obj.maxAscendingSum(nums)
print(out)