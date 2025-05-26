class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:

        out = []

        for i in range(2 ** len(nums)):
            bin_str = bin(i)[2:].zfill(len(nums))
            
            temp = []

            for index, bit in enumerate(bin_str):
                if(bit == "1"):
                    temp.append(nums[index])

            out.append(temp)

        return out
            

nums = [1,2,3]
obj = Solution()
out = obj.subsets(nums)
