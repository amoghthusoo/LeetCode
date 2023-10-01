class Solution:
    def removeDuplicates(self, nums: list) -> int:
        
        for num in nums:

            if (nums.count(num) > 2):

                while (nums.count(num) > 2):
                    nums.pop(nums.index(num))

        return len(nums)

nums = [0,0,1,1,1,1,2,3,3]
obj = Solution()
solution= obj.removeDuplicates(nums)
print(solution)
