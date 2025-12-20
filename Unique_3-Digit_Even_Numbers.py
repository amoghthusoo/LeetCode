from itertools import combinations, permutations
class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        
        even_digits = {"0", "2", "4", "6", "8"}
        comb_it = permutations(digits, 3)

        unique_nums = set()

        for c in comb_it:
            
            temp = ""
            for d in c:
                temp += str(d)

            temp = temp.lstrip("0")
        
            if(len(temp) == 3 and temp[-1] in even_digits):
                unique_nums.add(temp)
        
        return len(unique_nums)

digits = [0,2,2]
obj = Solution()
result = obj.totalNumbers(digits)
print(result)
