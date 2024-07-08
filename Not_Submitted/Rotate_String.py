class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        if(s == goal):
            return True

        i = 0
        while(i < len(s) - 1):

            rot_str = s[i + 1 : ] + s[0 : i + 1]

            if(rot_str == goal):
                return True 
            i += 1

        return False
    
s = "abcde"
goal = "cdeab"
obj = Solution()
out = obj.rotateString(s, goal)
print(out)