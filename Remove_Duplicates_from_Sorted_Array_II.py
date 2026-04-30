class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        INF = int(10 ** 4) + 1
        n = 0

        current = nums[0]
        count = 1
        i = 1
        while(i < len(nums)):
            
            if(nums[i] == current):
                count += 1
            else:
                current = nums[i]
                count = 1
            
            if(count > 2):
                nums[i] = INF
                n += 1

            i += 1

        nums.sort()
        return len(nums) - n

nums = [0,0,1,1,1,1,2,3,3]
obj = Solution()
result = obj.removeDuplicates(nums)
print(result)