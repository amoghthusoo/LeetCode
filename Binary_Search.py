class Solution:
    def search(self, nums: list[int], target: int) -> int:

        lower_bound = 0
        upper_bound = len(nums) - 1

        while(lower_bound <= upper_bound):


            mid = (lower_bound + upper_bound)//2

            if(nums[mid] == target):
                return mid
            
            if(nums[mid] > target):
                upper_bound = mid - 1
            else:
                lower_bound = mid + 1

        
        return -1
    

nums = [1, 2, 3, 4, 5]
target = 1
obj = Solution()
out = obj.search(nums, target)
print(out)