class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        
        visited = set()

        result = []
        for num in nums:
            if(num not in visited):
                visited.add(num)
            else:
                result.append(num)

        return result