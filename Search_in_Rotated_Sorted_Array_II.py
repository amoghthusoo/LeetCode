class Solution:
    def search(self, nums: list, target: int) -> bool:
        
        if (target in nums):
            return True
        else:
            return False



nums = [2,5,6,0,0,1,2]
target = 3
obj = Solution()
solution = obj.search(nums, target)
print(solution)