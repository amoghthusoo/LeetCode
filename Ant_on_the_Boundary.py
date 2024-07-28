class Solution:
    def returnToBoundaryCount(self, nums: list[int]) -> int:
        
        total = 0
        count = 0

        for num in nums:
            total += num

            if(total == 0):
                count += 1

        return count