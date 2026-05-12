class Solution:
    def checkDivisibility(self, n: int) -> bool:
        
        _sum = 0
        prod = 1
        for d in str(n):
            d = int(d)
            _sum += d
            prod *= d

        if(n % (_sum + prod) == 0):
            return True

        return False    

