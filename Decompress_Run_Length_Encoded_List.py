class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        
        ansList = []

        i = 0
        while (i < len(nums)):
            
            for j in range(nums[i]):
                ansList.append(nums[i + 1])
            
            i += 2

        return ansList

nums = [1,2,3,4]
obj = Solution()
solution = obj.decompressRLElist(nums)
print(solution)