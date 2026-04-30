class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)

        l1 = nums[-k :]
        l2 = nums[: -k]

        x = 0
        for e in l1:
            nums[x] = e
            x += 1
        
        for e in l2:
            nums[x] = e
            x += 1


nums = [1,2,3,4,5,6,7]
k = 3
obj = Solution()
obj.rotate(nums, k)
print(nums)
