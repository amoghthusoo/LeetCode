from itertools import permutations
class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        
        all_comb = list(permutations(digits, 3))

        all_nums = []

        for comb in all_comb:
            num_str = ""
            for num in comb:
                num_str += str(num)
            
            all_nums.append(int(num_str))
        
        filter_nums = []

        for num in all_nums:
            if(num % 2 == 0 and len(str(num)) == 3):
                filter_nums.append(num)

        filter_nums = list(set(filter_nums))

        filter_nums.sort()

        return filter_nums


digits = [2,1,3,0]
obj = Solution()
out = obj.findEvenNumbers(digits)
print(out)