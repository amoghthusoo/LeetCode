class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        
        negativeCount = 0
        zeroCount = 0

        for num in nums:
            
            if(num < 0):
                negativeCount += 1
            elif(num == 0):
                zeroCount += 1
            else:
                break

        positiveCount = len(nums) - negativeCount - zeroCount

        return max(positiveCount, negativeCount)

        


nums = [5,20,66,1314]
obj = Solution()
solution = obj.maximumCount(nums)
print(solution)