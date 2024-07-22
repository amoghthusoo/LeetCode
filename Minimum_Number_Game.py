class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        
        out_arr = []

        while(len(nums) != 0):
            alice_num = nums.pop(nums.index(min(nums)))
            bob_num = nums.pop(nums.index(min(nums)))

            out_arr.append(bob_num)
            out_arr.append(alice_num)

        return out_arr