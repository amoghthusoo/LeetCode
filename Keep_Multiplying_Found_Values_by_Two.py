class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        
        while True:

            if original in nums:
                original *= 2
            else:
                break
        
        return original

nums = [2,7,9]
original = 4
obj = Solution()
solution = obj.findFinalValue(nums, original)
print(solution)