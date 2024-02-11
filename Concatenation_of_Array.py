class Solution:
    def getConcatenation(self, nums: list) -> list:
        
        return nums * 2

nums = [1,3,2,1] 
obj = Solution()
solution = obj.getConcatenation(nums)
print(solution)