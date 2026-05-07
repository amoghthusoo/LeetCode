class Solution:
    def maxKDistinct(self, nums: list[int], k: int) -> list[int]:

        nums = sorted(list(set(nums)), reverse = True)

        ans = []
        i = 0
        while(i < min(len(nums), k)):
            ans.append(nums[i])
            i += 1

        return ans
        