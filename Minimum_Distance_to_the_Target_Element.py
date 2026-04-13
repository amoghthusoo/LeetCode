class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        
        indices = []
        for i, e in enumerate(nums):
            if(e == target):
                indices.append(i)

        ans = float("inf")

        for idx in indices:
            ans = min(ans, abs(idx - start))
        
        return ans