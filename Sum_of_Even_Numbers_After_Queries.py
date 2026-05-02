class Solution:
    def sumEvenAfterQueries(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        
        total = 0
        for e in nums:
            if(e % 2 == 0):
                total += e
        
        ans = []
        for q in queries:

            prev = nums[q[1]]
            nums[q[1]] += q[0]
            new = nums[q[1]]

            if(prev % 2 != 0 and new % 2 == 0):
                total += new
            elif(prev % 2 == 0 and new % 2 == 0):
                total += q[0]
            elif(prev % 2 == 0 and new % 2 != 0):
                total -= prev
            
            ans.append(total)
        
        return ans
            