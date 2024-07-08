class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        
        term1 = coordinates[0]
        term2 = coordinates[1]


        if((ord(term1) + int(term2)) % 2 == 0):
            return False
        else:
            return True