class Solution:
    def separateDigits(self, nums: list) -> list:
        
        ansList = []

        for element in nums:

            interList = []
            interList = list(str(element))

            i = 0
            while (i < len(interList)):
                
                interList[i] = int(interList[i])
                
                i += 1

            ansList += interList

        return ansList



nums = [7,1,3,9]
obj = Solution()
solution = obj.separateDigits(nums)
print(solution)