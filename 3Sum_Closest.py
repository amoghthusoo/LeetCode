class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        
        min_diff = abs(target - (nums[0] + nums[1] + nums[2]))
        ans = nums[0] + nums[1] + nums[2]
        
        nums.sort()
        i = 0
        while(i < len(nums) - 2):

            if(i != 0 and nums[i] == nums[i - 1]):
                i += 1
                continue
            
            
            j = i + 1
            k = len(nums) - 1

            while(j < k):

                if(j != i + 1 and nums[j] == nums[j - 1]):
                    j += 1
                    continue
                
                curr_sum = nums[i] + nums[j] + nums[k]

                diff = abs(target - curr_sum)
                if(diff < min_diff):
                    min_diff = diff
                    ans = curr_sum

                if(curr_sum < target):
                    j += 1
                elif(curr_sum > target):
                    k -= 1
                else:
                    return curr_sum
                    
            i += 1

        return ans
        
nums = [0,3,97,102,200]
target = 300
obj = Solution()
result = obj.threeSumClosest(nums, target)
print(result)