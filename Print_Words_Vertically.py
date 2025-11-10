class Solution:
    def printVertically(self, s: str) -> list[str]:
        
        words = s.split()

        n = len(words)

        m = -1
        for word in words:
            if(len(word) > m):
                m = len(word)
        
        mat = [[" " for _ in range(m)] for _ in range(n)]


        for i, word in enumerate(words):

            j = 0
            while(j < len(word)):
                
                mat[i][j] = word[j]
                j += 1
        
        ans = []

        for j in range(m):
            temp : str = ""
            for i in range(n):
                temp += mat[i][j]
            
            ans.append(temp.rstrip())
        
        return ans 

s = "TO BE OR NOT TO BE"
obj = Solution()
result = obj.printVertically(s)
print(result)