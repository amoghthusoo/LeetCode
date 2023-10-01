class Solution:
    def sortArrayByParity(self, nums: list) -> list:

        ansList = []

        for num in nums:
            if (num % 2 == 0):
                ansList.append(num)
        
        for num in nums:
            if (num % 2 != 0):
                ansList.append(num)

        return ansList
    
nums = [0]
obj = Solution()
solution = obj.sortArrayByParity(nums)
print(solution)