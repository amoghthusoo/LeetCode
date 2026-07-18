class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        
        x_count = y_count = 0
        for ch in s:
            if(ch == x):
                x_count += 1
            elif(ch == y):
                y_count += 1
        
        ans = ""
        ans += y * y_count
        ans += x * x_count

        for ch in s:
            if(ch != x and ch != y):
                ans += ch
        
        return ans