class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        
        prev = s
        new = s.replace("01", "10")

        ans = 0
        if(new != prev):
            ans += 1

        while(True):
            prev = new
            new = new.replace("01", "10")
            
            if(new != prev):
                ans += 1
            else:
                break
        
        return ans

s = "0110101"
obj = Solution()
result = obj.secondsToRemoveOccurrences(s)
print(result)
