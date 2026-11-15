class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()

        x = 0
        while(x < len(nums) - 3):

            if(x != 0 and nums[x] == nums[x - 1]):
                x += 1
                continue
            
            i = x + 1
            while(i < len(nums) - 2):
                
                if(i != x + 1 and nums[i] == nums[i - 1]):
                    i += 1
                    continue
                
                j = i + 1
                k = len(nums) - 1

                while(j < k):

                    if(j != i + 1 and nums[j] == nums[j - 1]):
                        j += 1
                        continue
                    
                    curr_sum = nums[x] + nums[i] + nums[j] + nums[k]

                    if(curr_sum < target):
                        j += 1
                    elif(curr_sum > target):
                        k -= 1
                    else:
                        ans.append([nums[x], nums[i], nums[j], nums[k]])
                        j += 1
        
                i += 1
            x += 1
        
        return ans