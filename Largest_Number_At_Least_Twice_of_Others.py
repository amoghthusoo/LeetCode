class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        
        largest_num = max(nums)
        largest_num_index = nums.index(largest_num)

        for i, num in enumerate(nums):
            
            if(i != largest_num_index):

                if(num * 2 > largest_num):
                    return -1
                
        return largest_num_index
