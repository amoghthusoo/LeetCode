class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:

        num_dict = {}

        for num in nums:
            num_dict[num] = None

        out_arr = []
        for i in range(1, len(nums) + 1):
            if(i not in num_dict):
                out_arr.append(i)

        return out_arr