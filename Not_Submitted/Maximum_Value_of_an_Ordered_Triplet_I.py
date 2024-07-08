class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:

        max_val = -(2 ** 31)
        
        i = 0
        while(i < len(nums) - 2):

            j = i + 1
            while(j < len(nums) - 1):

                k = j + 1
                while(k < len(nums)):
                    temp = (nums[i] - nums[j]) * nums[k]
                    if(temp > max_val):
                        max_val = temp

                    k += 1
                j += 1
            i += 1

        if(max_val < 0):
            return 0
        else:
            return max_val
