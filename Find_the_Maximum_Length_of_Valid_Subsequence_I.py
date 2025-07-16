class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        
        ans1 = 0
        for e in nums:
            if(e % 2 == 0):
                ans1 += 1
        
        ans2 = 0
        for e in nums:
            if(e % 2 != 0):
                ans2 += 1
        
        ans3 = 0
        remainder = 0
        for e in nums:
            if(e % 2 == remainder):
                ans3 += 1
                remainder ^= 1
        
        ans4 = 0
        remainder = 1
        for e in nums:
            if(e % 2 == remainder):
                ans4 += 1
                remainder ^= 1
        
        return max(ans1, ans2, ans3, ans4)