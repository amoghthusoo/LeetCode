class Solution:
    def findMaxConsecutiveOnes(self, nums: list) -> int:

        counter = 0
        interList = []
        i = 0
        while (i < len(nums)):

            
            if (nums[i] == 1):
                counter += 1
            elif (nums[i] == 0):
                if (counter != 0):
                    interList.append(counter)
                counter = 0
            
            if (i == len(nums) - 1):
                if (counter != 0):
                    interList.append(counter)
                counter = 0

            i += 1

        return max(interList)

nums = [1,0,1,1,0,1]
obj = Solution()
solution = obj.findMaxConsecutiveOnes(nums)
print(solution)