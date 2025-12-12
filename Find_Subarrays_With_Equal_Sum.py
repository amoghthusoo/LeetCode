class Solution:
    def findSubarrays(self, nums: list[int]) -> bool:
        
        visited = set()

        i = 1
        while(i < len(nums)):

            _sum = nums[i] + nums[i - 1]
            if(_sum not in visited):
                visited.add(_sum)
            else:
                return True

            i += 1
        
        return False