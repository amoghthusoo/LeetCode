class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        
        max_num = len(nums)

        occ_dict = {}

        for i in range(1, max_num + 1):
            occ_dict[i] = 0

        for e in nums:
            occ_dict[e] += 1

        ans = [None, None]

        for key, value in occ_dict.items():

            if(value == 2):
                ans[0] = key
            
            elif(value == 0):
                ans[1] = key
        
        return ans
    
nums = [1,1]
obj = Solution()
out = obj.findErrorNums(nums)
print(out)