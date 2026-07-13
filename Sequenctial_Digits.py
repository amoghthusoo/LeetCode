class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        
        digits = "123456789"
        ans = []
        for i in range(len(digits)):
            temp = ""
            for j in range(i, len(digits)):
                temp += digits[j]
                
                if(int(temp) >= low and int(temp) <= high):
                    ans.append(int(temp))
        
        return sorted(ans)
                
