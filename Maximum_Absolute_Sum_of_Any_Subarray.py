class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        
        INF = int(2 ** 32)

        a1 = -INF
        cs = 0
        for num in nums:
            cs += num
            if(cs < 0):
                cs = 0
            
            if(cs > a1):
                a1 = cs
        

        a2 = INF
        cs = 0
        for num in nums:
            cs += num

            if(cs > 0):
                cs = 0
            
            if(cs < a2):
                a2 = cs

        return max(abs(a1), abs(a2))