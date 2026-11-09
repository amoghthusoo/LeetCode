class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum_1 = 0
        zero_count_1 = 0
        for num in nums1:
            
            if(num == 0):
                zero_count_1 += 1
            else:
                sum_1 += num
        
        sum_2 = 0
        zero_count_2 = 0
        for num in nums2:
            
            if(num == 0):
                zero_count_2 += 1
            else:
                sum_2 += num

        min_sum_1 = sum_1 + zero_count_1
        min_sum_2 = sum_2 + zero_count_2

        if(min_sum_1 == min_sum_2):
            return min_sum_1

        elif(min_sum_1 < min_sum_2):
            if(zero_count_1 > 0):
                return min_sum_2
            else:
                return -1
            
        else:
            if(zero_count_2 > 0):
                return min_sum_1
            else:
                return -1