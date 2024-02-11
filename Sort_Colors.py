class Solution:
    def sortColors(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0
        while (i < len(nums) - 1):
            j = 0
            while (j < len(nums) - 1):

                if (nums[j] > nums[j + 1]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

                j += 1
            i += 1

        
        return None

nums = [2,0,1]
obj = Solution()
solution = obj.sortColors(nums)
print(solution)