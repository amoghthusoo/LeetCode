class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = len(nums) - 2
        while(i >= 0 and nums[i] >= nums[i + 1]):
            i -= 1

        if(i < 0):
            nums.sort()
            return nums

        j = i + 1
        smallest = nums[j]
        idx = i + 1
        while(j < len(nums)):

            if(nums[j] > nums[i] and nums[j] < smallest):
                smallest = nums[j]
                idx = j

            j += 1

        nums[i], nums[idx] = nums[idx], nums[i]

        subarr = nums[i + 1 : ]
        subarr.sort()
        nums[i + 1 : ] = subarr

nums = [2,3,1,3,3]
obj = Solution()
result = obj.nextPermutation(nums)
print(result)