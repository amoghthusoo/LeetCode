class Solution:
    def transformArray(self, nums: list[int]) -> list[int]:
        
        even_count = 0
        for num in nums:
            if(num % 2 == 0):
                even_count += 1

        odd_count = len(nums) - even_count

        result = []
        for _ in range(even_count):
            result.append(0)
        for _ in range(odd_count):
            result.append(1)

        return result