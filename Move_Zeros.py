class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        # METHOD 1
        # i = 0
        # while (i < len(nums) - 1):
            
        #     j = 0
        #     while(j < len(nums) - 1):
                
        #         if (nums[j] == 0):
        #             nums[j], nums[j + 1] = nums[j + 1], nums[j]
                
        #         j += 1
        #     i += 1

        counter = 0

        try:
            while(True):
                nums.pop(nums.index(0))
                counter += 1
        except:

            for i in range(counter):
                nums.append(0)
        


        return nums



nums = [0,1,0,3,12]
obj = Solution()
solution = obj.moveZeroes(nums)
print(solution)