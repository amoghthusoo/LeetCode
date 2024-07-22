class Solution:
    def maxOperations(self, nums: list[int]) -> int:
        
        operations = 0
        score = nums[0] + nums[1]
        nums.pop(0)
        nums.pop(0)
        operations += 1

        while(len(nums) >= 2):

            temp_score = nums[0] + nums[1]

            if(temp_score == score):
                nums.pop(0)
                nums.pop(0)
                operations += 1
            else:
                break

        return operations



