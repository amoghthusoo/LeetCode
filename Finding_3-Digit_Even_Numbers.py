from itertools import permutations

class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        
        x = permutations(digits, 3)
        result = set()

        while(True):
            try:
                e = x.__next__()
                if(e[0] != 0 and e[-1] % 2 == 0):
                    result.add(int(str(e[0]) + str(e[1]) + str(e[2]))) 
            except:
                break
        
        return sorted(list(result))
        

digits = [2,1,3,0]
solution = Solution()
result = solution.findEvenNumbers(digits)
print(result)
