class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        
        ans = float("inf")
        i = 0 
        while(i < len(nums)):

            j = i + 1
            while(j < len(nums)):

                if((nums[i] == 1 and nums[j] == 2) or (nums[i] == 2 and nums[j] == 1)):
                    diff = j - i
                    if(diff < ans):
                        ans = diff

                j += 1
            i += 1

        if(ans == float("inf")):
            return -1
        else:
            return ans