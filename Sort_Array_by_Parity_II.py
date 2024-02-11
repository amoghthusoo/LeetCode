class Solution:
    def sortArrayByParityII(self, nums: list) -> list:
        
        evenList = []
        oddList = []
        ansList = []

        for num in nums:

            if (num % 2 == 0):
                evenList.append(num)
            else:
                oddList.append(num)

        i = 0
        while (i < len(evenList)):
            ansList.append(evenList[i])
            ansList.append(oddList[i])
            i += 1

        return ansList
    

nums = [2,3]
obj = Solution()
solution = obj.sortArrayByParityII(nums)
print(solution)