class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:

        g.sort()
        s.sort()
        count = 0

        i = 0
        j = 0
        while(i < len(g) and j < len(s)):

            while(j < len(s) and s[j] < g[i]):
                j += 1
            
            if(j < len(s)):
                i += 1
                j += 1
                count += 1

        return count

g = [1,2,3]
s = [1,1]
obj = Solution()
result = obj.findContentChildren(g, s)
print(result)