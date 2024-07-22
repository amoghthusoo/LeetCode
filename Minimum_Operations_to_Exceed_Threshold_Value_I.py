class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        
        count = 0

        for e in nums:
            if(e < k):
                count += 1

        return count