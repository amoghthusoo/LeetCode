from collections import Counter
class Solution:
    def findLHS(self, nums: list[int]) -> int:
        
        occr_dict = Counter(nums)
        sorted_items = sorted(occr_dict.items())

        max_len = 0

        i = 0
        while(i < len(sorted_items) - 1):
            
            if(sorted_items[i + 1][0] == sorted_items[i][0] + 1):
                temp_len = sorted_items[i][1] + sorted_items[i + 1][1]

                if(temp_len > max_len):
                    max_len = temp_len

            i += 1

        return max_len
