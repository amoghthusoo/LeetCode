class Solution:
    def smallestAbsent(self, nums: list[int]) -> int:

        avg = sum(nums)/len(nums)
        nums = set(nums)

        i = int(avg) + 1
        while(True):

            if(i not in nums and i > 0):
                return i
            
            i += 1
