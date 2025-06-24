class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        
        indices = set()

        for i, e in enumerate(nums):

            if(e == key):
                j = i - k
                if(j < 0):
                    j = 0
                while(j <= i + k and j < len(nums)):
                    indices.add(j)
                    j += 1
        
        return sorted(list(indices))
            
nums = [2,2,2,2,2]
key = 2
k = 2
obj = Solution()
result = obj.findKDistantIndices(nums, key, k)
print(result)