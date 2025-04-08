from collections import Counter

class Solution:

    def unique_elements_exists(self, occr_dict : dict):

        for val in occr_dict.values():
            
            if(val >= 2):
                return False
            
        return True

    def minimumOperations(self, nums: list[int]) -> int:    

        occr_dict = dict(Counter(nums))
        count = 0
        i = 0
        while(i < len(nums)):

            if(self.unique_elements_exists(occr_dict)):
                return count
            
            try:
                occr_dict[nums[i]] -= 1 
                occr_dict[nums[i + 1]] -= 1 
                occr_dict[nums[i + 2]] -= 1
            except:
                pass
            finally:
                count += 1
            
            if(self.unique_elements_exists(occr_dict)):
                return count
            
            i += 3

nums = [1,2,3,4,2,3,3,5,7]
solution = Solution()
result = solution.minimumOperations(nums)
print(result)