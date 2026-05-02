class Solution:
    def rotatedDigits(self, n: int) -> int:
        
        def get_rotated(n):
            rot = ""
            n = str(n)
            for digit in n:
                if(digit in {"0", "1", "8"}):
                    rot += digit
                elif(digit == "2"):
                    rot += "5"
                elif(digit == "5"):
                    rot += "2"
                elif(digit == "6"):
                    rot += "9"
                elif(digit == "9"):
                    rot += "6"
                else:
                    return False
            
            return int(rot)
        
        ans = 0
        for i in range(1, n + 1):

            rotated = get_rotated(i)
            if(rotated and rotated != i):
                ans += 1

        return ans