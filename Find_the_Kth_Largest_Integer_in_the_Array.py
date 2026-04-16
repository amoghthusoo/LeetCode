class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:

        for i, e in enumerate(nums):
            nums[i] = int(e)
        nums.sort(reverse = True)
        return str(nums[k - 1])






