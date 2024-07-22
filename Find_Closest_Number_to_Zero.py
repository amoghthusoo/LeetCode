class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        
        distance_dict = {}

        for num in nums:
            distance_dict[num] = abs(num)

        min_distance = min(distance_dict.values())

        possible_ans = []

        for key, value in distance_dict.items():
            
            if(value == min_distance):
                possible_ans.append(key)

        return max(possible_ans)