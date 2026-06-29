class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        
        i = 0
        while(i < len(nums)):

            j = 0
            while(j < len(nums)):

                if(abs(i - j) >= indexDifference and 
                   abs(nums[i] - nums[j]) >= valueDifference):
                    return [i, j]

                j += 1
            i += 1
        
        return [-1, -1]