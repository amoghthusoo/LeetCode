class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        
        max_diff = -1

        i = 0
        while(i < len(nums)):

            j = i + 1
            while(j < len(nums)):

                if(nums[j] > nums[i]):
                    diff = nums[j] - nums[i]

                    if(diff > max_diff):
                        max_diff = diff

                j += 1
            i += 1

        return max_diff