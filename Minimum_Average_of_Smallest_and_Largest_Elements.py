class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        
        averages = []

        while(len(nums) != 0):

            min_element = nums.pop(nums.index(min(nums)))
            max_element = nums.pop(nums.index(max(nums)))
            averages.append((min_element + max_element) / 2)


        return min(averages)