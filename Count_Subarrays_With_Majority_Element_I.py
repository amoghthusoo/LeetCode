class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        
        ans = 0

        i = 0
        while(i < len(nums)):

            occr_dict = dict()
            j = i
            while(j < len(nums)):
                
                occr_dict[nums[j]] = occr_dict.get(nums[j], 0) + 1

                sub_arr_len = j - i + 1
                target_cnt = occr_dict.get(target, 0)

                if(target_cnt > sub_arr_len/2):
                    ans += 1

                j += 1
            i += 1
        
        return ans