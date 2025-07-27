class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        
        current = nums[0]
        nums_mod = [current]
        i = 1
        while(i < len(nums)):

            if(nums[i] != current):
                nums_mod.append(nums[i])
                current = nums[i]

            i += 1

        ans = 0
        i = 1
        while(i < len(nums_mod) - 1):

            if(
                (nums_mod[i - 1] < nums_mod[i] and nums_mod[i + 1] < nums_mod[i]) or 
                (nums_mod[i - 1] > nums_mod[i] and nums_mod[i + 1] > nums_mod[i])
            ):
                ans += 1
            i += 1

        return ans

nums = [2,4,1,1,6,5]
obj = Solution()
result = obj.countHillValley(nums)
print(result)