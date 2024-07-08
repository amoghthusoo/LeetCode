from collections import Counter

class Solution:
    def isGood(self, nums: list[int]) -> bool:

        if(len(nums) == 1):
            return False
        
        occr_dict = dict(Counter(nums))
        
        i = 1
        while(i < len(nums)):

            if(i != len(nums) - 1):

                try:
                    if(occr_dict[i] != 1):
                        return False
                except:
                    return False
                
            else:

                try:
                    if(occr_dict[i] != 2):
                        return False
                except:
                    return False
                
            i += 1

        return True
    
nums = [1, 3, 3, 2]
obj = Solution()
out = obj.isGood(nums)
print(out)
    