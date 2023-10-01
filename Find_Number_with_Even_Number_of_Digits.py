class Solution:
    def findNumbers(self, nums: list) -> int:
        
        count = 0

        for element in nums:

            if len(str(element)) % 2 == 0:
                count += 1

        return count



arr = [555,901,482,1771]
obj = Solution()
solution = obj.findNumbers(arr)
print(solution)