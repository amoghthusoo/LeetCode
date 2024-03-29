class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        
        count_dict = {0:-1}
        count = 0
        maxLength = 0

        for i in range(len(nums)):
            
            if(nums[i] == 0):
                count -= 1
            elif(nums[i] == 1):
                count += 1

            if(count in count_dict):
                length = i - count_dict[count]
                if(length > maxLength):
                    maxLength = length

            else:
                count_dict[count] = i
        
        return maxLength

nums = [0, 0, 0]
obj = Solution()
out = obj.findMaxLength(nums)
print(out)