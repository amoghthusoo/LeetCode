class Solution:
    def sumOfThree(self, num: int) -> list[int]:
        
        if(num % 3 == 0):
            x = num // 3
            return [x - 1, x, x + 1]
        else:
            return []