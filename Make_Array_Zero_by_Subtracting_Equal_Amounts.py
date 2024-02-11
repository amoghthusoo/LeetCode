class Solution:
    def minimumOperations(self, nums: list) -> int:
        
        count = 0

        while (0 in nums):
            nums.pop(nums.index(0))

        while (len(nums) != 0):

            minNum = min(nums)

            i = 0
            while (i < len(nums)):
                
                nums[i] = nums[i] - minNum
                i += 1

            while (0 in nums):
                nums.pop(nums.index(0))

            count += 1    

        return count


nums = [0]
obj = Solution()
solution = obj.minimumOperations(nums)
print(solution)
