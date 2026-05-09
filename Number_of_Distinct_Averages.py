class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        
        seen = set()
        nums.sort()

        i = 0
        j = len(nums) - 1
        while(i <= j):
            seen.add((nums[i] + nums[j])/2)

            i += 1
            j -= 1
        
        return len(seen)
