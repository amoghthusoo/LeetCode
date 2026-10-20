class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
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