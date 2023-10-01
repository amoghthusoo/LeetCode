class Solution:
    def differenceOfSum(self, nums: list) -> int:
        
        elementSum = 0
        digitSum = 0

        for element in nums:

            elementSum += element

            for digit in str(element):
                digitSum += int(digit)
        
        return abs(elementSum - digitSum)


nums = [1,2,3,4]
obj = Solution()
solution = obj.differenceOfSum(nums)
print(solution)