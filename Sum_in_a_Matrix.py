class Solution:
    def matrixSum(self, nums: list[list[int]]) -> int:
        
        for i in range(len(nums)):
            nums[i].sort(reverse = True)
        
        ans = 0
        for j in range(len(nums[0])):
            _max = 0
            for i in range(len(nums)):
                if(nums[i][j] > _max):
                    _max = nums[i][j]
            
            ans += _max
        
        return ans


nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]
obj = Solution()
result = obj.matrixSum(nums)
print(result)