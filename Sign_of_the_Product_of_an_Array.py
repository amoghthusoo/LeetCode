class Solution:
    def arraySign(self, nums: list) -> int:
        
        if (0 in nums):
            return 0
        else:
            negNums = 0
            for num in nums:
                if (num < 0):
                    negNums += 1
            
            if (negNums % 2 == 0):
                return 1
            else:
                return -1

nums = [-1,1,-1,1,-1]
obj = Solution()
solution = obj.arraySign(nums)
print(solution)