class Solution:
    def averageValue(self, nums: list[int]) -> int:

        acc, cnt = 0, 0
        for num in nums:

            if(num % 6 == 0):
                acc += num 
                cnt += 1
        
        return acc//cnt if cnt != 0 else 0
        
    