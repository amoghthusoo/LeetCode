class Solution:
    def minimumMoves(self, s: str) -> int:
        
        s = [ch for ch in s]
        ans = 0
        i = 0
        while(i <= len(s) - 3):
            
            if(s[i] == "X"):
                ans += 1
                s[i + 1] = "O"
                s[i + 2] = "O"
            
            i += 1

        if(s[i] == "X" or s[i + 1] == "X"):
            ans += 1
        
        return ans