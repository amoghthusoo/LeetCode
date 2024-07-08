class Solution:
    def secondHighest(self, s: str) -> int:
        
        digits = []

        for letter in s:
            
            if(letter.isdigit()):
                digits.append(int(letter))

        digits = list(set(digits))
        
        if(len(digits) <= 1):
            return -1
        else:
            digits.sort()
            return digits[-2]

        
