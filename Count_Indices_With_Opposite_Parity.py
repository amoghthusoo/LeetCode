class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        
        ans = []
        for i in range(len(nums)):
            temp = 0
            for j in range(i + 1, len(nums)):

                if(nums[i] % 2 == 0 and nums[j] % 2 == 1):
                    temp += 1
                
                elif(nums[i] % 2 != 0 and nums[j] % 2 == 0):
                    temp += 1
            
            ans.append(temp)
            
        return ans

nums = [1,2,3,4]
obj = Solution()
result = obj.countOppositeParity(nums)
print(result)