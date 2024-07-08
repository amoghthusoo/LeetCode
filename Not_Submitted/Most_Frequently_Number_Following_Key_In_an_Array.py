from collections import Counter

class Solution:
    def mostFrequent(self, nums: list[int], key: int) -> int:
        
        inter_list = []

        i = 0
        while(i < len(nums) - 1):

            if(nums[i] == key):
                inter_list.append(nums[i + 1])

            i += 1

        occr_dict = dict(Counter(inter_list))

        max_occur = max(occr_dict.values())

        for key, value in occr_dict.items():
            
            if(value == max_occur):
                return key

