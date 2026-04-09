class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        ans = []

        nums.sort()
        i = 0
        while(nums[i] <= 0 and i < len(nums) - 2):

            if(i != 0 and nums[i] == nums[i - 1]):
                i += 1
                continue
            
            target = -nums[i]
            j = i + 1
            k = len(nums) - 1

            while(j < k):
                
                if(j != i + 1 and nums[j] == nums[j - 1]):
                    j += 1
                    continue

                if(nums[j] + nums[k] < target):
                    j += 1
                elif(nums[j] + nums[k] > target):
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1

            i += 1

        return ans
        
nums = [0,0,0]
obj = Solution()
result = obj.threeSum(nums)
print(result)