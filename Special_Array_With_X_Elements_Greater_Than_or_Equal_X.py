class Solution:

    def greater_equal(self, nums, k):

        cnt = 0
        for num in nums:
            if(num >= k):
                cnt += 1
        return cnt

    def specialArray(self, nums: list[int]) -> int:
        
        i = 0
        while(i <= len(nums)):
            cnt = self.greater_equal(nums, i)
            if(cnt == i):
                return i
            i += 1
        
        return -1