class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        prefix = ""
        _max = ""
        
        for digit in num:
            
            prefix += digit

            if(int(digit) % 2 != 0):
                _max = prefix
            

        return _max
