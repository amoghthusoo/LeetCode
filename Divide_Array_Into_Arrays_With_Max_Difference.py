class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        
        nums.sort()
        ans = []
        for i in range(0, len(nums), 3):

            if(
                abs(nums[i] - nums[i + 1]) <= k and
                abs(nums[i + 1] - nums[i + 2]) <= k and
                abs(nums[i] - nums[i + 2]) <= k
            ):
                ans.append([nums[i], nums[i + 1], nums[i + 2]])
            else:
                return []
        
        return ans